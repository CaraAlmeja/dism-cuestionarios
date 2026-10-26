import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {runInNewContext} from 'node:vm';
import * as core from '../public/core.js';
import {createQuizShortcuts} from '../public/shortcuts.js';
import {renderGuide} from '../public/guide.js';

const data=JSON.parse(readFileSync(new URL('../public/data/questions.json',import.meta.url),'utf8'));
const source=readFileSync(new URL('../public/app.js',import.meta.url),'utf8')
  .replace(/^import .*;\r?$/gm,'')
  .replaceAll('import.meta.url',JSON.stringify(new URL('../public/app.js',import.meta.url).href));

// Run the actual renderer and actions with isolated storage and minimal DOM controls.
async function openQuiz(active,storedState=null,route='quiz') {
  const initial=storedState??{...core.emptyState(),active};
  const storage=new Map([[core.STORAGE_KEY,JSON.stringify(initial)]]);
  const elements=new Map();
  const element=selector=>{
    if(!elements.has(selector))elements.set(selector,{
      innerHTML:'',textContent:'',dataset:{},focus(){},addEventListener(){}
    });
    return elements.get(selector);
  };
  const main=element('main');main.querySelector=()=>null;
  let hash=`#${route}`;
  const location={get hash(){return hash;},set hash(value){hash=`#${value.replace(/^#/, '')}`;}};
  const context={...core,createQuizShortcuts,renderGuide,URL,console,location,
    document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){},body:{dataset:{}}},
    window:{addEventListener(){},scrollTo(){}},matchMedia:()=>({matches:true}),
    fetch:async()=>({ok:true,json:async()=>data}),
    localStorage:{getItem:key=>storage.get(key)??null,setItem:(key,value)=>storage.set(key,value)}
  };
  const app=await runInNewContext(`(async()=>{${source}\nreturn {actions,render};})()`,context);
  assert.match(main.innerHTML,route==='quiz'?/class="quiz-card"/:/class="review-item/,'the application must load the requested page');
  return {...app,get html(){return main.innerHTML;},
    saved:()=>JSON.parse(storage.get(core.STORAGE_KEY)),
    refresh(){app.render();}
  };
}

const topic=html=>html.match(/<span class="tag">(.*?)<\/span>/s)?.[1];
const blockCode=q=>data.blocks.find(b=>b.id===q.block).code;
const questions=['t1-17','t1-18'].map(id=>data.questions.find(q=>q.id===id));
const escaped=value=>value.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

test('ninguna pregunta revela su etiqueta antes de corregir, en estudio ni en examen',async()=>{
  for(const mode of ['study','exam']) {
    const session=core.createSession(data.questions,{source:'all',mode});
    const app=await openQuiz(session);
    for(const [index,q] of data.questions.entries()) {
      app.actions.jump({dataset:{index:String(index)}});
      assert.equal(topic(app.html),blockCode(q),`${mode}: ${q.id}`);
      assert.ok(!app.html.includes('class="feedback'));
      assert.equal((app.html.match(/role="radio"/g)||[]).length,4);
    }
  }
});

test('estudio: seleccionar no revela el tema; comprobar lo muestra y conserva la corrección al volver y recargar',async()=>{
  const [q,next]=questions;
  for(const correct of [false,true]) {
    const session=core.createSession(questions,{source:'t1',mode:'study'});
    const app=await openQuiz(session);
    const answer=correct?q.correct_option_id:q.options.find(o=>o.id!==q.correct_option_id).id;
    app.actions.answer({dataset:{id:answer}});
    assert.equal(topic(app.html),blockCode(q));
    assert.deepEqual(app.saved().stats,{});
    const pending=await openQuiz(null,app.saved());
    assert.equal(topic(pending.html),blockCode(q));
    pending.actions.check();
    assert.equal(topic(pending.html),`${blockCode(q)} · ${q.tag}`);
    assert.ok(pending.html.includes(q.explanation));
    assert.equal(pending.saved().stats[q.id].lastCorrect,correct);
    await pending.actions.next();
    assert.equal(topic(pending.html),blockCode(next));
    pending.actions.previous();
    assert.equal(topic(pending.html),`${blockCode(q)} · ${q.tag}`);
    const restored=await openQuiz(null,pending.saved());
    assert.equal(topic(restored.html),`${blockCode(q)} · ${q.tag}`);
    assert.equal(restored.saved().active.answers[q.id],answer);
  }
});

test('examen: responder, navegar y reanudar ocultan etiquetas y soluciones hasta finalizar',async()=>{
  const [q,next]=questions;
  const app=await openQuiz(core.createSession(questions,{source:'t1',mode:'exam'}));
  app.actions.answer({dataset:{id:q.correct_option_id}});
  assert.equal(topic(app.html),blockCode(q));
  await app.actions.next();
  assert.equal(topic(app.html),blockCode(next));
  app.actions.answer({dataset:{id:next.correct_option_id}});
  app.actions.previous();
  const restored=await openQuiz(null,app.saved());
  assert.equal(topic(restored.html),blockCode(q));
  assert.ok(!restored.html.includes('class="feedback'));
  assert.deepEqual(restored.saved().stats,{});
  await restored.actions.finish();
  restored.refresh();
  assert.equal(restored.saved().active,null);
  assert.equal(restored.saved().history[0].correct,2);
  assert.ok(restored.html.includes('Respuesta correcta:'));
  assert.ok(restored.html.includes(q.explanation));
  for(const reason of Object.values(q.distractor_rationales))assert.ok(restored.html.includes(escaped(reason)));
});

test('acertar permite comparar las tres alternativas incorrectas en el orden mostrado en todo el banco',async()=>{
  const session=core.createSession(data.questions,{source:'all',mode:'study'});
  const app=await openQuiz(session);
  for(const [index,q] of data.questions.entries()) {
    app.actions.jump({dataset:{index:String(index)}});
    app.actions.answer({dataset:{id:q.correct_option_id}});
    assert.ok(!app.html.includes('class="alternative-feedback"'));
    app.actions.check();
    assert.ok(app.html.includes(escaped(q.explanation)),q.id);
    assert.match(app.html,/<details class="alternative-feedback"><summary>Por qué las otras opciones son incorrectas<\/summary>/);
    const list=app.html.match(/<ul class="alternative-list">(.*?)<\/ul>/s)[1];
    assert.equal((list.match(/<li>/g)||[]).length,3,q.id);
    let previous=-1;
    for(const id of session.items[index].order.filter(id=>id!==q.correct_option_id)) {
      const option=q.options.find(o=>o.id===id);
      const position=list.indexOf(`<strong>${escaped(option.text)}</strong>`);
      assert.ok(position>previous,`${q.id}: orden de alternativas`);
      assert.ok(list.includes(escaped(q.distractor_rationales[id])),`${q.id}: motivo de ${id}`);
      previous=position;
    }
    assert.ok(!list.includes('(Tu respuesta)'));
  }
});

test('al fallar mantiene el motivo inmediato y permite comparar las tres alternativas incorrectas',async()=>{
  const q=questions[0],wrong=q.options.find(o=>o.id!==q.correct_option_id);
  const app=await openQuiz(core.createSession([q],{source:'single',mode:'study'}));
  app.actions.answer({dataset:{id:wrong.id}});
  app.actions.check();
  assert.ok(app.html.includes(`<strong>Por qué tu respuesta no encaja:</strong> ${escaped(q.distractor_rationales[wrong.id])}`));
  assert.ok(app.html.includes(`<strong>${escaped(wrong.text)}</strong> <span class="alternative-chosen">(Tu respuesta)</span>`));
  for(const reason of Object.values(q.distractor_rationales))assert.ok(app.html.includes(escaped(reason)));
});

test('la revisión de una pregunta en blanco también explica todas las alternativas sin inventar una respuesta',async()=>{
  const q=questions[0];
  const session=core.createSession([q],{source:'single',mode:'exam'});
  const app=await openQuiz(null,{...core.emptyState(),lastResult:session},'resultado');
  assert.ok(app.html.includes('<strong>Tu respuesta:</strong> Sin responder'));
  assert.ok(app.html.includes('Para tu próximo intento'));
  assert.ok(!app.html.includes('Por qué tu respuesta no encaja:'));
  assert.ok(!app.html.includes('(Tu respuesta)'));
  assert.ok(app.html.includes(escaped(q.explanation)));
  for(const reason of Object.values(q.distractor_rationales))assert.ok(app.html.includes(escaped(reason)));
});
