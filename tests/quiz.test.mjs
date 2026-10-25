import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {emptyState,selectQuestions,createSession,recordAnswer,failedIds,summarize,gradeSession,validateState} from '../public/core.js';
const {questions:bank,blocks,retired_question_ids:retiredIds}=JSON.parse(readFileSync(new URL('../public/data/questions.json',import.meta.url),'utf8'));
const expectedCounts={t1:19,t21:33,t22:31,t31:32,t32:19,t4:1};
const byId=Object.fromEntries(bank.map(q=>[q.id,q]));
test('135 preguntas en seis bloques, cuatro opciones y referencias completas',()=>{
  assert.equal(bank.length,135);assert.equal(new Set(bank.map(q=>q.id)).size,135);assert.equal(blocks.length,6);
  for(const b of blocks) {
    const qs=bank.filter(q=>q.block===b.id);assert.equal(qs.length,expectedCounts[b.id]);
    const positions=[0,0,0,0];
    for(const q of qs) {
      assert.equal(q.options.length,4);assert.equal(new Set(q.options.map(o=>o.id)).size,4);assert.equal(new Set(q.options.map(o=>o.text)).size,4);
      const correct=q.options.findIndex(o=>o.id===q.correct_option_id);assert.ok(correct>=0);positions[correct]++;
      assert.ok(q.explanation.length>30);assert.ok(q.source_pages.length);
      if(q.source_type==='web')assert.ok(q.reference_url.startsWith('https://www.openapis.org/'));
      else assert.ok(q.source_file.endsWith('.pdf'));
      assert.deepEqual(Object.keys(q.distractor_rationales).sort(),q.options.filter(o=>o.id!==q.correct_option_id).map(o=>o.id).sort());
    }
    assert.ok(Math.max(...positions)-Math.min(...positions)<=1);
  }
});
test('mezcla de 20 sin duplicados, OpenAPI una vez y reparto del resto entre los cinco bloques',()=>{
  for(let attempt=0;attempt<25;attempt++) {
    const chosen=selectQuestions(bank,'mixed');assert.equal(chosen.length,20);assert.equal(new Set(chosen.map(q=>q.id)).size,20);
    assert.equal(chosen.filter(q=>q.block==='t4').length,1);
    const counts=blocks.filter(b=>b.id!=='t4').map(b=>chosen.filter(q=>q.block===b.id).length);
    assert.ok(counts.every(n=>n===3||n===4));
  }
  assert.equal(selectQuestions(bank,'all',bank.length).length,135);
  assert.equal(selectQuestions(bank,'t4').length,1);
});
test('la clave sigue al ID con cualquier orden y no cambia el banco original',()=>{
  const snapshot=JSON.stringify(bank);
  for(let i=0;i<20;i++) {
    const s=createSession(bank.filter(q=>q.block==='t1'),{source:'t1'});
    const positions=[0,0,0,0];
    for(const item of s.items){const q=byId[item.id];positions[item.order.indexOf(q.correct_option_id)]++;s.answers[item.id]=q.correct_option_id;}
    assert.ok(Math.max(...positions)-Math.min(...positions)<=1);assert.equal(gradeSession(s,byId).correct,expectedCounts.t1);
  }
  assert.equal(JSON.stringify(bank),snapshot);
});
test('un fallo entra en repaso y un acierto posterior lo retira sin perder historial',()=>{
  const state=emptyState(),q=bank[0],wrong=q.options.find(o=>o.id!==q.correct_option_id).id;
  recordAnswer(state,q,wrong);assert.deepEqual(failedIds(state),[q.id]);
  recordAnswer(state,q,q.correct_option_id);assert.deepEqual(failedIds(state),[]);
  assert.equal(state.stats[q.id].attempts,2);assert.equal(state.stats[q.id].wrong,1);assert.equal(summarize(state,bank).accuracy,50);assert.equal(summarize(state,bank).seen,1);
});
test('las sesiones de una sola pregunta no fijan la solución en A',()=>{
  const first=createSession([bank[0]],{source:'single'},()=>0);
  const last=createSession([bank[0]],{source:'single'},()=>.999);
  assert.notEqual(first.items[0].order.indexOf(bank[0].correct_option_id),last.items[0].order.indexOf(bank[0].correct_option_id));
});
test('mantiene el orden lógico de opciones numéricas durante la sesión',()=>{
  const ordered=bank.filter(q=>q.shuffle_options===false);assert.ok(ordered.length>0);
  for(const q of ordered){
    const numbers=q.options.map(o=>{
      const text=o.text.match(/^[\d\s.,/]+/)[0].replaceAll(' ','').replace(',','.');
      const [a,b]=text.split('/').map(Number);return b?a/b:a;
    });
    assert.equal(new Set(numbers).size,4,`${q.id}: opciones numéricamente equivalentes`);
    assert.deepEqual(numbers,[...numbers].sort((a,b)=>a-b),`${q.id}: orden numérico incorrecto`);
  }
  const s=createSession(ordered,{source:'all'});
  for(const item of s.items)assert.deepEqual(item.order,byId[item.id].options.map(o=>o.id));
});
test('examen: elegir respuesta no registra ni revela la corrección; blancos separados',()=>{
  const state=emptyState(),s=createSession(bank.slice(0,3),{source:'t1',mode:'exam'});
  s.answers[s.items[0].id]=byId[s.items[0].id].correct_option_id;
  s.answers[s.items[1].id]=byId[s.items[1].id].options.find(o=>o.id!==byId[s.items[1].id].correct_option_id).id;
  assert.deepEqual(s.submitted,[]);assert.deepEqual(state.stats,{});
  assert.deepEqual(gradeSession(s,byId),{correct:1,wrong:1,blank:1,total:3,percent:33});
});
test('se recuperan orden, respuestas y correcciones de una sesión',()=>{
  const state=emptyState(),q=bank[0];state.active=createSession(bank.slice(0,4),{source:'t1'});
  state.active.answers[q.id]=q.correct_option_id;state.active.submitted.push(q.id);state.active.recorded.push(q.id);recordAnswer(state,q,q.correct_option_id);
  const restored=validateState(JSON.parse(JSON.stringify(state)),bank);assert.deepEqual(restored,state);
  assert.equal(gradeSession(restored.active,byId).correct,1);
});
test('importación: rechaza contadores inválidos y descarta sesiones ajenas o corruptas',()=>{
  const state=emptyState();assert.throws(()=>validateState({},bank));
  recordAnswer(state,bank[0],bank[0].correct_option_id);state.stats[bank[0].id].attempts=-1;assert.throws(()=>validateState(state,bank));
  state.stats={};state.active=createSession(bank.slice(0,2),{source:'t1'});state.active.items[0].order=['bad'];assert.equal(validateState(state,bank).active,null);
  state.active=createSession(bank.slice(0,2),{source:'t1'});assert.equal(validateState(state,bank,{includeSessions:false}).active,null);
  state.active.answers['unknown-id']='o1';assert.equal(validateState(state,bank).active,null);
});
test('el repaso selecciona solo IDs pendientes y admite listas cortas',()=>{
  const ids=[bank[3].id,bank[25].id];assert.deepEqual(selectQuestions(bank,'errors',20,ids).map(q=>q.id).sort(),ids.sort());assert.deepEqual(selectQuestions(bank,'errors',20,[]),[]);
});
test('recalcula ejercicios numéricos contra valores independientes',()=>{
  const correct=id=>{const q=byId[id];return q.options.find(o=>o.id===q.correct_option_id).text;};
  assert.equal(parseInt('1011',2)^parseInt('0101',2)^parseInt('1100',2),parseInt(correct('t22-05'),2));
  assert.equal(parseInt('0010',2)^parseInt('1011',2)^parseInt('1100',2),parseInt(correct('t22-06'),2));
  assert.equal(parseInt('0010',2)^parseInt('1100',2)^parseInt('1000',2),parseInt(correct('t22-07'),2));
  assert.equal((5-1)*2,8);assert.equal(512*512*24/8/2**20,.75);
  assert.equal(2**2+1**2+2*1,7);assert.equal(420/7,60);assert.equal(84/7*420,5040);assert.equal(33000/(25*2)/4,165);
  assert.equal((3*7)**(4/2)/6,73.5);assert.ok(Math.abs(2*Math.sqrt(21)-9.17)<.01);
  assert.equal(600*3/(3*60),10);assert.equal((25-15)/25,.4);assert.ok(Math.abs(500*4/180-11.11)<.01);
  assert.equal(Number.parseFloat(correct('t21-28')),8/(4-2));
  assert.equal(correct('t21-32'),`Unicast: ${100*8} Mbit/s; multicast: 8 Mbit/s`);
  assert.equal(Number.parseInt(correct('t22-23')),Buffer.byteLength('A'.repeat(100),'utf8'));
  assert.equal(Buffer.byteLength('一','utf8'),3);assert.equal(Buffer.byteLength('一','utf16le'),2);
});
test('las exportaciones de alumno y solucionario coinciden con cada clave final',()=>{
  for(const b of blocks){
    const student=readFileSync(new URL(`../public/exports/${b.id}/cuestionario.md`,import.meta.url),'utf8');
    const solution=readFileSync(new URL(`../public/exports/${b.id}/solucionario.md`,import.meta.url),'utf8');
    const questions=bank.filter(q=>q.block===b.id);
    questions.forEach((q,i)=>{
      const position=q.options.findIndex(o=>o.id===q.correct_option_id),letter=String.fromCharCode(65+position),text=q.options[position].text;
      assert.ok(student.includes(q.stem));assert.ok(!student.includes(q.explanation));
      assert.ok(solution.includes(`## ${i+1}. ${letter}) ${text}`));assert.ok(solution.includes(q.explanation));
      for(const reason of Object.values(q.distractor_rationales))assert.ok(solution.includes(reason));
    });
  }
});
test('exclusiones de la segunda guía y definición única de OpenAPI',()=>{
  assert.equal(retiredIds.length,4);
  assert.ok(retiredIds.every(id=>!byId[id]));
  assert.ok(!JSON.stringify(bank).includes('Flutter'));
  assert.ok(!bank.some(q=>['Generaciones móviles','Generaciones WiFi','Funcionamiento sin conexión'].includes(q.tag)));
  const t4=bank.filter(q=>q.block==='t4');assert.equal(t4.length,1);assert.equal(t4[0].stem,'¿Qué es OpenAPI?');
  const counts=[0,0,0,0];for(const q of bank)counts[q.options.findIndex(o=>o.id===q.correct_option_id)]++;
  assert.ok(Math.max(...counts)-Math.min(...counts)<=1);
});
test('la actualización conserva respuestas vigentes de una sesión con una pregunta retirada',()=>{
  const state=emptyState(),obsolete={...bank[0],id:'t1-14'};
  state.active=createSession([bank[0],obsolete,bank[1]],{source:'t1'});
  state.active.index=2;
  for(const q of [bank[0],obsolete]){state.active.answers[q.id]=q.correct_option_id;state.active.submitted.push(q.id);state.active.recorded.push(q.id);recordAnswer(state,q,q.correct_option_id);}
  const restored=validateState(JSON.parse(JSON.stringify(state)),bank,{retiredIds});
  assert.equal(restored.active.items.length,2);assert.equal(restored.active.index,1);
  assert.equal(restored.active.items[1].id,bank[1].id);
  assert.deepEqual(restored.active.submitted,[bank[0].id]);assert.deepEqual(Object.keys(restored.stats),[bank[0].id]);
  assert.equal(restored.active.answers[bank[0].id],bank[0].correct_option_id);
});
test('una sesión compuesta solo por preguntas retiradas se cierra sin borrar otros aciertos',()=>{
  const state=emptyState(),obsolete={...bank[0],id:'t1-14'};
  state.active=createSession([obsolete],{source:'t1'});recordAnswer(state,bank[0],bank[0].correct_option_id);
  const restored=validateState(state,bank,{retiredIds});assert.equal(restored.active,null);assert.equal(restored.stats[bank[0].id].correct,1);
});
