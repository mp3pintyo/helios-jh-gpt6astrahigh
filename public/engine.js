const status=document.getElementById('status');
const tell=(state,extra={})=>parent.postMessage({type:'helios-state',state,...extra},location.origin);
globalThis.heliosConfig={embedded:true,scene:'model',screenPercentage:75,gpuBudgetMs:20,gi:'lite',statusElement:'status'};
let api,ready=false,rotating=false,paused=false,renderPaused=false,settleUntil=0,angle=.58,last=0;
const camera=()=>api.heliosLookAt(Math.sin(angle)*7.7,7.3,Math.cos(angle)*7.7,0,.65,0);
try {
 if(!navigator.gpu)throw Error('Ebben a böngészőben nem érhető el a WebGPU.');
 api=await import('./helios/pkg/helios_demo.js');
 await api.default();
 const started=performance.now();
 const poll=setInterval(()=>{
  if(api.heliosReady() && api.heliosFrames()>0){
   clearInterval(poll);ready=true;camera();settleUntil=performance.now()+1800;tell('ready',{scene:api.heliosScene()});
  }else if(performance.now()-started>90000){clearInterval(poll);tell('error',{message:status.textContent||'A motor indítása túllépte az időkorlátot.'});}
 },250);
 new MutationObserver(()=>{if(/error|failed|unsupported|Could not|panicked/i.test(status.textContent))tell('error',{message:status.textContent});}).observe(status,{childList:true,subtree:true,characterData:true});
 function animate(t){if(ready){const nextPaused=paused||(!rotating&&t>settleUntil&&api.heliosBusy()==='');if(nextPaused!==renderPaused){renderPaused=nextPaused;api.heliosSetPaused(renderPaused)}if(rotating&&!paused){angle+=Math.min(t-last,60)*.00012;camera();}}last=t;requestAnimationFrame(animate)}requestAnimationFrame(animate);
 window.addEventListener('message',e=>{if(e.origin!==location.origin||e.source!==parent)return;const m=e.data;if(!ready)return;if(m.type==='rotate'){rotating=m.value;settleUntil=performance.now()+1000}if(m.type==='pause'){if(paused&&!m.value)settleUntil=performance.now()+1400;paused=m.value}if(m.type==='reset'){angle=.58;camera();settleUntil=performance.now()+1000}if(m.type==='view'){api.heliosSetView(m.value);settleUntil=performance.now()+1000}});
 window.addEventListener('resize',()=>{settleUntil=performance.now()+1400});
 window.heliosDiagnostics=()=>({scene:api.heliosScene(),hud:api.heliosHud(),ready,rotating,paused,renderPaused});
}catch(e){tell('error',{message:String(e.message||e)});}
