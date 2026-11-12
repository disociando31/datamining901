/* Visualizador de flujos exportados por Orange. Sin dependencias y sin ejecutar modelos. */
(function(){'use strict';
const NS='http://www.w3.org/2000/svg';
const el=(tag,attrs={},text)=>{const o=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>o.setAttribute(k,v));if(text!==undefined)o.textContent=text;return o};
const HELP_URL='/static/etapa6/flow_help.json';
const card=document.querySelector('.co-flow-panel');if(!card)return;
Promise.all([fetch(card.dataset.flowUrl).then(r=>{if(!r.ok)throw Error('flows');return r.json()}),fetch(HELP_URL).then(r=>r.json())]).then(([all,help])=>{
 const flow=all[card.dataset.flow],h=help[card.dataset.flow]||{},svg=card.querySelector('svg'),scroller=card.querySelector('.co-flow-scroller'),detail=card.querySelector('.co-widget-detail');
 if(!flow||!flow.nodes.length)throw Error('Sin nodos');
 let scale=1;const nodes=flow.nodes.map(n=>({...n,x:n.x,y:n.y}));const minX=Math.min(...nodes.map(n=>n.x)),minY=Math.min(...nodes.map(n=>n.y));
 nodes.forEach(n=>{n.x=(n.x-minX)*1.22+40;n.y=(n.y-minY)*1.22+40});
 const byId=Object.fromEntries(nodes.map(n=>[n.id,n]));const width=Math.max(...nodes.map(n=>n.x))+190,height=Math.max(...nodes.map(n=>n.y))+110;
 svg.setAttribute('viewBox',`0 0 ${width} ${height}`);svg.setAttribute('width',width);svg.setAttribute('height',height);
 const defs=el('defs'),marker=el('marker',{id:'co-arrow',viewBox:'0 0 10 10',refX:'9',refY:'5',markerWidth:'5',markerHeight:'5',orient:'auto-start-reverse'});marker.append(el('path',{d:'M 0 0 L 10 5 L 0 10 z',fill:'#57718a'}));defs.append(marker);svg.append(defs);
 const edgeGroup=el('g'),nodeGroup=el('g');svg.append(edgeGroup,nodeGroup);const edgeEls=[];
 flow.edges.forEach(e=>{const a=byId[e.source],b=byId[e.target];if(!a||!b)return;const sameX=Math.abs(a.x-b.x)<65;const x1=a.x+(sameX?75:145),y1=a.y+(sameX?52:25),x2=b.x+(sameX?75:0),y2=b.y+(sameX?0:25);const dx=(x2-x1)*.5;let path;
 if(sameX){path=`M${a.x+75} ${a.y+52} C${a.x+75} ${y1+36} ${b.x+75} ${y2-36} ${b.x+75} ${b.y}`;}else{path=`M${x1} ${y1} C${x1+dx} ${y1} ${x2-dx} ${y2} ${x2} ${y2}`;}
 const p=el('path',{d:path,class:'co-flow-edge'});edgeGroup.append(p);edgeEls.push({p,e});});
 const records=[];
 function activate(n,g){records.forEach(x=>x.g.classList.toggle('is-active',x.n.id===n.id));edgeEls.forEach(x=>x.p.classList.toggle('is-active',x.e.source===n.id||x.e.target===n.id));const incoming=flow.edges.filter(e=>e.target===n.id).map(e=>byId[e.source]?.name).filter(Boolean),outgoing=flow.edges.filter(e=>e.source===n.id).map(e=>byId[e.target]?.name).filter(Boolean);
 detail.replaceChildren();const head=document.createElement('strong');head.textContent=n.name;detail.append(head);const p=document.createElement('p');p.textContent=h[n.name]||'Widget presente en el flujo original de Orange.';detail.append(p);const small=document.createElement('small');small.textContent=`Entradas: ${incoming.join(', ')||'ninguna'} · Salidas: ${outgoing.join(', ')||'ninguna'}`;small.style.color='#93a4ba';detail.append(small);}
 nodes.forEach(n=>{const g=el('g',{class:'co-flow-node',transform:`translate(${n.x},${n.y})`,tabindex:'0',role:'button','aria-label':`Ver widget ${n.name}`});g.append(el('rect',{width:145,height:52}));g.append(el('text',{x:12,y:15,class:'node-num'},`WIDGET ${Number(n.id)+1}`));const name=n.name.length>23?n.name.slice(0,21)+'…':n.name;g.append(el('text',{x:12,y:36,class:'node-title'},name));g.addEventListener('click',()=>activate(n,g));g.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();activate(n,g)}});nodeGroup.append(g);records.push({n,g})});
 function zoom(step){scale=Math.max(.55,Math.min(1.8,scale+step));svg.style.width=`${width*scale}px`;svg.style.height=`${height*scale}px`};zoom(0);
 card.querySelector('.co-flow-zoomin').addEventListener('click',()=>zoom(.15));card.querySelector('.co-flow-zoomout').addEventListener('click',()=>zoom(-.15));card.querySelector('.co-flow-reset').addEventListener('click',()=>{scale=1;zoom(0);scroller.scrollTo({left:0,top:0,behavior:'smooth'})});
 let down=false,sx=0,sy=0,sl=0,st=0;scroller.addEventListener('pointerdown',e=>{if(e.target.closest('.co-flow-node'))return;down=true;sx=e.clientX;sy=e.clientY;sl=scroller.scrollLeft;st=scroller.scrollTop});scroller.addEventListener('pointermove',e=>{if(!down)return;scroller.scrollLeft=sl-(e.clientX-sx);scroller.scrollTop=st-(e.clientY-sy)});window.addEventListener('pointerup',()=>{down=false});
 }).catch(()=>{card.querySelector('.co-flow-scroller').textContent='No fue posible cargar el diagrama. Revisa que estén publicados los archivos flows.json y flow_help.json.'});
})();
