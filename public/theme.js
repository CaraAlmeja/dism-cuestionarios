(() => {
  const key='dism-lab:theme';
  const root=document.documentElement;
  const valid=value=>value==='light'||value==='dark';
  function apply(theme) {
    root.dataset.theme=theme;
    const dark=theme==='dark';
    document.querySelector('meta[name="theme-color"]')?.setAttribute('content',dark?'#14141e':'#f7f8fb');
    const toggle=document.querySelector('#theme-toggle');
    if(!toggle)return;
    toggle.setAttribute('aria-pressed',String(dark));
    toggle.setAttribute('aria-label',dark?'Cambiar a tema claro':'Cambiar a tema oscuro');
    toggle.title=dark?'Cambiar a tema claro':'Cambiar a tema oscuro';
    toggle.querySelector('.theme-label').textContent=dark?'Oscuro':'Claro';
  }
  let initial='dark';
  try{const saved=localStorage.getItem(key);if(valid(saved))initial=saved;}catch{}
  apply(initial);
  document.addEventListener('DOMContentLoaded',()=>{
    apply(root.dataset.theme);
    document.querySelector('#theme-toggle').addEventListener('click',()=>{
      const theme=root.dataset.theme==='dark'?'light':'dark';
      apply(theme);
      try{localStorage.setItem(key,theme);}catch{}
    });
  });
  window.addEventListener('storage',event=>{
    if(event.key===key)apply(valid(event.newValue)?event.newValue:'dark');
  });
})();
