// El keyup también se consume: Comprobar cambia el foco a Siguiente y
// el navegador no debe activar ese nuevo botón al soltar Espacio.
export function createQuizShortcuts({getContext,selectOption,check,next,isDialogOpen,onError=()=>{}}) {
  const held=new Set();
  const normalize=key=>key===' '||key==='Spacebar'?'Space':key;
  const invoke=action=>{try{Promise.resolve(action()).catch(onError);}catch(error){onError(error);}};
  function keydown(event) {
    const key=normalize(event.key);
    if(held.has(key)){event.preventDefault();return;}
    if(event.defaultPrevented||event.isComposing||event.ctrlKey||event.altKey||event.metaKey||isDialogOpen())return;
    const target=event.target;
    if(target?.closest('input,select,textarea,[contenteditable]:not([contenteditable="false"]),[role="textbox"]'))return;
    const context=getContext();
    if(!context)return;
    const control=target?.closest('button,a,summary,label');
    const action=control?.dataset?.action;
    if(control&&!['answer','check','next'].includes(action))return;
    if(/^[1-4]$/.test(key)) {
      event.preventDefault();
      if(event.repeat)return;
      held.add(key);invoke(()=>selectOption(Number(key)-1));return;
    }
    if(key!=='Space'&&key!=='Enter')return;
    // Tab + Espacio/Enter sigue permitiendo elegir una opción sin seleccionar.
    if(action==='answer'&&control.getAttribute('aria-pressed')!=='true')return;
    event.preventDefault();
    if(event.repeat)return;
    held.add(key);
    if(context.mode==='study'&&!context.submitted) {
      if(context.hasAnswer)invoke(check);
    } else invoke(next);
  }
  function keyup(event) {
    const key=normalize(event.key);
    if(held.delete(key))event.preventDefault();
  }
  return {keydown,keyup,reset:()=>held.clear()};
}
