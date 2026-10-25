export const STORAGE_KEY = 'dism-lab:v1';
export function emptyState() {return {version:1,stats:{},history:[],active:null,lastResult:null};}
export function shuffle(items, random=Math.random) {
  const result=[...items];
  for(let i=result.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[result[i],result[j]]=[result[j],result[i]];}
  return result;
}
export function selectQuestions(bank, source, count=20, ids=null) {
  if(ids) return shuffle(bank.filter(q=>ids.includes(q.id))).slice(0,count);
  if(source==='mixed') {
    const blocks=[...new Set(bank.map(q=>q.block))];
    const buckets=blocks.map(b=>shuffle(bank.filter(q=>q.block===b)));
    const selected=[];
    while(selected.length<Math.min(count,bank.length) && buckets.some(b=>b.length)) {
      for(const bucket of shuffle(buckets)) {if(bucket.length && selected.length<count) selected.push(bucket.pop());}
    }
    return shuffle(selected);
  }
  return shuffle(source==='all'?bank:bank.filter(q=>q.block===source)).slice(0,count);
}
export function createSession(questions, {source,mode='study',title='Cuestionario'},random=Math.random) {
  const counts=[0,0,0,0],free=[];
  for(const q of questions)if(q.shuffle_options===false)counts[q.options.findIndex(o=>o.id===q.correct_option_id)]++;
  for(const q of questions)if(q.shuffle_options!==false){
    const minimum=Math.min(...counts),choices=[0,1,2,3].filter(i=>counts[i]===minimum);
    const position=choices[Math.floor(random()*choices.length)];free.push(position);counts[position]++;
  }
  const positions=shuffle(free,random);
  const items=questions.map(q=>{
    if(q.shuffle_options===false)return {id:q.id,order:q.options.map(o=>o.id)};
    const wrong=shuffle(q.options.filter(o=>o.id!==q.correct_option_id).map(o=>o.id),random);
    wrong.splice(positions.pop(),0,q.correct_option_id);
    return {id:q.id,order:wrong};
  });
  return {id:crypto.randomUUID(),source,mode,title,items,index:0,answers:{},submitted:[],recorded:[],startedAt:new Date().toISOString()};
}
export function recordAnswer(state,question,optionId,now=new Date().toISOString()) {
  if(!question.options.some(o=>o.id===optionId)) throw new Error('Respuesta desconocida');
  const correct=optionId===question.correct_option_id;
  const previous=state.stats[question.id]||{attempts:0,correct:0,wrong:0};
  state.stats[question.id]={attempts:previous.attempts+1,correct:previous.correct+Number(correct),wrong:previous.wrong+Number(!correct),lastCorrect:correct,lastAt:now};
  return correct;
}
export function failedIds(state) {return Object.entries(state.stats).filter(([,s])=>s.lastCorrect===false).map(([id])=>id);}
export function summarize(state,bank) {
  const entries=bank.map(q=>state.stats[q.id]).filter(Boolean);
  const attempts=entries.reduce((s,x)=>s+x.attempts,0);
  const correct=entries.reduce((s,x)=>s+x.correct,0);
  return {seen:entries.length,mastered:entries.filter(s=>s.lastCorrect).length,attempts,correct,accuracy:attempts?Math.round(correct/attempts*100):0,failed:entries.filter(s=>!s.lastCorrect).length};
}
export function gradeSession(session,byId) {
  let correct=0,wrong=0,blank=0;
  for(const item of session.items) {
    const answer=session.answers[item.id];
    if(!answer) blank++;
    else if(answer===byId[item.id].correct_option_id) correct++;
    else wrong++;
  }
  return {correct,wrong,blank,total:session.items.length,percent:Math.round(correct/session.items.length*100)};
}
export function validateState(input, bank, {includeSessions=true,retiredIds=[]}={}) {
  if(!input || input.version!==1 || typeof input.stats!=='object' || input.stats===null || Array.isArray(input.stats)) throw new Error('Formato de progreso no compatible');
  const result=emptyState();
  const byId=Object.fromEntries(bank.map(q=>[q.id,q]));
  for(const [id,s] of Object.entries(input.stats)) {
    if(!Object.hasOwn(byId,id)) continue;
    if(!s || ![s.attempts,s.correct,s.wrong].every(n=>Number.isSafeInteger(n)&&n>=0&&n<=1000000) || s.attempts!==s.correct+s.wrong || !s.attempts || typeof s.lastCorrect!=='boolean' || !Number.isFinite(Date.parse(s.lastAt))) throw new Error('El archivo contiene estadísticas inválidas');
    result.stats[id]={attempts:s.attempts,correct:s.correct,wrong:s.wrong,lastCorrect:s.lastCorrect,lastAt:s.lastAt};
  }
  result.history=(Array.isArray(input.history)?input.history:[]).filter(h=>h && typeof h.id==='string' && Number.isFinite(Date.parse(h.finishedAt)) && ['study','exam'].includes(h.mode) && [h.correct,h.wrong,h.blank,h.total].every(n=>Number.isInteger(n)&&n>=0&&n<=bank.length) && h.total>0 && h.correct+h.wrong+h.blank===h.total && typeof h.title==='string').slice(-200).map(h=>({id:h.id,title:h.title.slice(0,120),mode:h.mode,source:String(h.source).slice(0,30),correct:h.correct,wrong:h.wrong,blank:h.blank,total:h.total,finishedAt:h.finishedAt}));
  function validSession(s) {
    if(!s || typeof s.id!=='string' || typeof s.title!=='string' || !['study','exam'].includes(s.mode) || !Array.isArray(s.items) || !s.items.length || s.items.length>bank.length || !Number.isInteger(s.index) || s.index<0 || s.index>=s.items.length || !s.answers || typeof s.answers!=='object' || !['submitted','recorded'].every(k=>Array.isArray(s[k])) || !Number.isFinite(Date.parse(s.startedAt))) return false;
    const ids=new Set();
    for(const item of s.items){
      const q=byId[item.id];
      if(!q || ids.has(item.id) || !Array.isArray(item.order) || item.order.length!==4 || new Set(item.order).size!==4 || item.order.some(id=>!q.options.some(o=>o.id===id)))return false;
      ids.add(item.id);
    }
    if(Object.entries(s.answers).some(([id,answer])=>!ids.has(id)||!byId[id].options.some(o=>o.id===answer))) return false;
    if([...s.submitted,...s.recorded].some(id=>!ids.has(id)||!s.answers[id]) || new Set(s.submitted).size!==s.submitted.length || new Set(s.recorded).size!==s.recorded.length)return false;
    return true;
  }
  function migrateSession(session) {
    if(!session||!Array.isArray(session.items)||!session.answers||!Array.isArray(session.submitted)||!Array.isArray(session.recorded))return session;
    const retired=new Set(retiredIds);
    if(!session.items.some(item=>retired.has(item.id)))return session;
    const items=session.items.filter(item=>!retired.has(item.id));
    if(!items.length)return null;
    const currentId=session.items[session.index]?.id;
    const currentIndex=items.findIndex(item=>item.id===currentId);
    const ids=new Set(items.map(item=>item.id));
    return {...session,items,index:currentIndex>=0?currentIndex:Math.min(Math.max(session.index,0),items.length-1),
      answers:Object.fromEntries(Object.entries(session.answers).filter(([id])=>ids.has(id))),
      submitted:session.submitted.filter(id=>ids.has(id)),recorded:session.recorded.filter(id=>ids.has(id))};
  }
  if(includeSessions) {
    const active=migrateSession(input.active),lastResult=migrateSession(input.lastResult);
    if(validSession(active))result.active=active;
    if(validSession(lastResult))result.lastResult=lastResult;
  }
  return result;
}
