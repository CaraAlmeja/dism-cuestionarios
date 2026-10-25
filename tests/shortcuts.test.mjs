import test from 'node:test';
import assert from 'node:assert/strict';
import {createQuizShortcuts} from '../public/shortcuts.js';

function target({action,selected=false,editable=false,other=false,index=0}={}) {
  const control=action||other?{dataset:{action,index:String(index)},getAttribute:()=>String(selected)}:null;
  return {closest:selector=>selector.startsWith('input,')?(editable?{}:null):control};
}
function event(key,options={}) {
  return {key,target:target(),repeat:false,defaultPrevented:false,
    preventDefault(){this.defaultPrevented=true;},...options};
}
function setup(overrides={}) {
  const calls=[];
  const context={mode:'study',submitted:false,hasAnswer:true,...overrides};
  let dialog=false;
  const shortcuts=createQuizShortcuts({
    getContext:()=>context,
    selectOption:index=>calls.push(['select',index]),
    check:()=>{calls.push(['check']);context.submitted=true;},
    next:()=>calls.push(['next']),
    isDialogOpen:()=>dialog
  });
  return {shortcuts,calls,context,setDialog:value=>{dialog=value;}};
}

test('Espacio confirma una sola vez y consume keyup aunque cambie el foco a Siguiente',()=>{
  const {shortcuts,calls}=setup();
  const down=event(' ',{target:target({action:'answer',selected:true})});
  shortcuts.keydown(down);
  const repeat=event(' ',{repeat:true,target:target({action:'next'})});shortcuts.keydown(repeat);
  const up=event(' ',{target:target({action:'next'})});shortcuts.keyup(up);
  assert.deepEqual(calls,[['check']]);
  assert.ok(down.defaultPrevented&&repeat.defaultPrevented&&up.defaultPrevented);
  shortcuts.keydown(event(' ',{target:target({action:'next'})}));
  assert.deepEqual(calls,[['check'],['next']]);
});
test('mantener Enter tampoco salta preguntas tras corregir',()=>{
  const {shortcuts,calls}=setup();
  shortcuts.keydown(event('Enter'));
  for(let i=0;i<10;i++)shortcuts.keydown(event('Enter',{repeat:true,target:target({action:'next'})}));
  assert.deepEqual(calls,[['check']]);
  shortcuts.keyup(event('Enter'));
  shortcuts.keydown(event('Enter',{target:target({action:'next'})}));
  assert.deepEqual(calls,[['check'],['next']]);
});
test('no confirma una pregunta sin respuesta ni desplaza la página al pulsar Espacio',()=>{
  const {shortcuts,calls}=setup({hasAnswer:false});const down=event(' ');
  shortcuts.keydown(down);assert.deepEqual(calls,[]);assert.ok(down.defaultPrevented);
});
test('en examen Espacio continúa sin ejecutar la corrección de estudio',()=>{
  const {shortcuts,calls}=setup({mode:'exam'});shortcuts.keydown(event(' '));
  assert.deepEqual(calls,[['next']]);
});
test('Tab y Espacio pueden seleccionar una opción aún no marcada con la activación nativa',()=>{
  const {shortcuts,calls}=setup();const down=event(' ',{target:target({action:'answer',selected:false})});
  shortcuts.keydown(down);assert.equal(down.defaultPrevented,false);assert.deepEqual(calls,[]);
});
test('no roba el teclado a formularios, enlaces, otros botones, modificadores o diálogos',()=>{
  for(const options of [{target:target({editable:true})},{target:target({other:true})},{target:target({action:'previous'})},{ctrlKey:true},{altKey:true},{metaKey:true},{isComposing:true}]) {
    const {shortcuts,calls}=setup(),down=event(' ',options);shortcuts.keydown(down);
    assert.deepEqual(calls,[]);assert.equal(down.defaultPrevented,false);
  }
  const {shortcuts,calls,setDialog}=setup();setDialog(true);const down=event(' ');
  shortcuts.keydown(down);assert.deepEqual(calls,[]);assert.equal(down.defaultPrevented,false);
});
test('soltar una tecla iniciada en el test no activa un diálogo que se acaba de abrir',()=>{
  const {shortcuts,setDialog}=setup();shortcuts.keydown(event(' '));setDialog(true);
  const up=event(' ',{target:target({other:true})});shortcuts.keyup(up);assert.ok(up.defaultPrevented);
});
test('las teclas 1–4 no repiten selecciones mientras se mantienen pulsadas',()=>{
  const {shortcuts,calls}=setup();shortcuts.keydown(event('3'));shortcuts.keydown(event('3',{repeat:true}));
  shortcuts.keyup(event('3'));shortcuts.keydown(event('4'));
  assert.deepEqual(calls,[['select',2],['select',3]]);
});
test('perder el foco libera teclas para que la siguiente pulsación funcione',()=>{
  const {shortcuts,calls}=setup();shortcuts.keydown(event(' '));shortcuts.reset();shortcuts.keydown(event(' '));
  assert.deepEqual(calls,[['check'],['next']]);
});
test('flechas recorren las cuatro respuestas únicas, con vuelta al principio y sin corregir',()=>{
  const {shortcuts,calls}=setup();
  shortcuts.keydown(event('ArrowRight',{target:target({action:'answer',index:3})}));
  shortcuts.keyup(event('ArrowRight'));
  shortcuts.keydown(event('ArrowLeft',{target:target({action:'answer',index:0})}));
  shortcuts.keyup(event('ArrowLeft'));
  shortcuts.keydown(event('ArrowDown',{target:target({action:'answer',index:1})}));
  shortcuts.keyup(event('ArrowDown'));
  shortcuts.keydown(event('ArrowUp',{target:target({action:'answer',index:2})}));
  assert.deepEqual(calls,[['select',0],['select',3],['select',2],['select',1]]);
});
test('las flechas no cambian una pregunta ya corregida ni controles ajenos al grupo',()=>{
  const {shortcuts,calls}=setup({submitted:true});
  shortcuts.keydown(event('ArrowRight',{target:target({action:'answer',index:1})}));
  shortcuts.keydown(event('ArrowLeft',{target:target({other:true})}));
  assert.deepEqual(calls,[]);
});
test('Espacio respeta Dejar para después sin comprobar ni necesitar una selección',()=>{
  for(const hasAnswer of [false,true]) {
    const {shortcuts,calls}=setup({hasAnswer});
    const down=event(' ',{target:target({action:'next'})});
    shortcuts.keydown(down);shortcuts.keydown(event(' ',{repeat:true,target:target({action:'next'})}));
    shortcuts.keyup(event(' ',{target:target({action:'next'})}));
    assert.ok(down.defaultPrevented);assert.deepEqual(calls,[['next']]);
  }
});
