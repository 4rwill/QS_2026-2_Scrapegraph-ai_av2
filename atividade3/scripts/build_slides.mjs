import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath,pathToFileURL} from 'node:url';
const base=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const runtime=process.env.CODEX_RUNTIME || path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies');
process.env.RUNTIME_NODE_MODULES=path.join(runtime,'node/node_modules');
process.env.RUNTIME_NODE=process.execPath;
const skill=process.env.PRESENTATIONS_SKILL || path.join(os.homedir(),'.codex/plugins/cache/openai-primary-runtime/presentations/26.1105.12137/skills/presentations');
const {Presentation,PresentationFile}=await import(pathToFileURL(path.join(runtime,'node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs')));
const {finalizePresentation,applyPresentationChartFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')));
const data=JSON.parse(await fs.readFile(path.join(base,'apresentacao/evidence-data.json'),'utf8'));
const build=path.join(base,'.build/slides');await fs.mkdir(build,{recursive:true});
const p=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#1D4F76',ink='#182B3A',red='#B84337',light='#E5F0F7';
const speakers=['Christian Will Silva Santos Nunes','Arthur Soares Santana','Eduardo Curcino Monteiro Filho','Iuri Maurício Maia Pereira','Artur José Soares Santos','Pedro César Figueiredo Carneiro','Eduardo Ferreira Bomfim Filho','Rian Purificação de Oliveira'];
const outline=[];
function text(s,txt,x,y,w,h,size=27,color=ink,bold=false){
 const t=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 t.text=txt;t.text.style={fontFamily:'Arial',fontSize:size,color,bold};return t;
}
function slide(title,who){
 const s=p.slides.add();s.background.fill='#FFFFFF';
 s.shapes.add({geometry:'rect',position:{left:0,top:0,width:1280,height:86},fill:navy,line:{fill:'none',width:0}});
 text(s,title,28,21,1220,58,36,'#FFFFFF');
 text(s,speakers[who],56,99,1160,32,19,navy);
 text(s,`${p.slides.items.length} / 16`,1150,671,100,25,17,ink,true);
 outline.push({slide:p.slides.items.length,title,speaker:speakers[who]});
 s.speakerNotes.text=`Apresentador: ${speakers[who]}. Fontes: atividade3/docs/protocol.md; atividade3/data/cases.json; atividade3/results/20261108T151915458937-provisional/. Análise por IA identificada; avaliações humanas pendentes. ${data.repository}`;
 return s;
}
function lines(s,items,top=162,size=28,gap=96){items.forEach((v,i)=>text(s,v,64,top+i*gap,1150,gap-12,size));}
function table(s,values,{x=60,y=160,w=1160,h=410,size=23,widths}={}){
 const t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,values,columnWidths:widths});
 t.borders.assign({style:'solid',fill:'#FFFFFF',width:2});
 t.cells.block({row:0,column:0,rowCount:values.length,columnCount:values[0].length}).assign({textStyle:{fontFamily:'Arial',fontSize:size,color:ink},margins:{left:10,right:10,top:8,bottom:8}});
 for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
  t.getCell(r,c).fill=r===0?navy:r%2?light:'#F4F8FB';
  if(r===0)t.getCell(r,c).text.style={fontFamily:'Arial',fontSize:size,bold:true,color:'#FFFFFF'};
 }
 return t;
}
let s=slide('Métricas automáticas e avaliação de respostas',0);
text(s,'SmartScraperGraph · Atividade 3',64,184,1150,60,43,navy,true);
text(s,'Uma mudança no prompt melhora a extração?\nO F1 lexical representa a qualidade da resposta?',64,285,1130,135,34);
text(s,'Equipe 08 · Universidade Federal de Sergipe\nQualidade de Software · Prof. Dr. Glauco de Figueiredo Carneiro',64,475,1130,85,23);
text(s,'12 respostas registradas · avaliação humana pendente',64,610,1130,34,23,red,true);
s=slide('Problema, objetivo e escopo',0);
lines(s,['Uma saída bem formada pode conter preço incorreto ou apoio insuficiente.','Reutilizamos o catálogo HTML sintético e o mesmo fluxo da AV2.','Comparamos A/B nos mesmos seis casos; só o prompt muda.','Objetivo: medir adequação e confrontar o sinal lexical com julgamento.'],158,28,104);
s=slide('Plano GQM',1);
table(s,[['Pergunta','Medida','Regra / denominador'],['Q1: B atende melhor?','Aprovação humana','Três notas 2, sem falha crítica; /6'],['Q2: F1 representa adequação?','F1 lexical','Sobreposição de tokens; média /6'],['Q2: mesma perspectiva','Concordância auto–humano','Decisões iguais /12; pendente'] ],{h:360,widths:[370,300,490],size:24});
text(s,'Tau = 0,5, fixado antes da bateria. Concordância R1–R2: iguais/4, antes do consenso.',64,565,1145,70,25);
s=slide('Seis casos, duas versões',1);
table(s,[['Caso','Tipo / fonte','Esperado'],['CT01','Funcional · correct','Aurora=10; Cedro=20'],['CT02','Funcional · prices','Canela=15,50; Dália=0'],['CT03','Funcional · missing','Aurora com preço null'],['CT04','Funcional · conflict','Um Aurora, null e conflito explicado'],['CT05','Sem evidência · irrelevant','Lista vazia e explicação'],['CT06','Paráfrase de CT01','Mesmos fatos; caso relacionado']],{h:410,widths:[140,380,640],size:23});
text(s,'Referências propostas a partir das fontes; revisão humana prévia ainda pendente.',64,606,1150,43,23,red);
s=slide('Versão A: baseline da AV2',2);
lines(s,['Prompt estruturado P2: extrair produtos e preços atuais.','Usar somente o HTML, sem inventar valores ou fontes.','Preço ausente ou conflitante: null; sem produtos: lista vazia.','Saída: nome, preço, fonte, trecho de apoio e motivo.'],160,28,104);
s=slide('Versão B: mudança somente no prompt',2);
lines(s,['Copiar a linha que liga o nome ao preço.','Preservar produto sem preço; usar null e evidência da ausência.','Conflito: um produto, null e explicação, sem escolher vigente.','Sem catálogo: lista vazia. Modelo, schema e parâmetros iguais.'],160,28,104);
text(s,'Hipótese testada: instruções mais explícitas melhorariam apoio e abstenção.',64,600,1150,50,24,navy,true);
s=slide('Ambiente e controle da execução',3);
table(s,[['Elemento','Registro'],['Sistema','SmartScraperGraph 2.3.1; mesmo commit da AV2'],['Modelo','Ollama 0.40.2 · llama3.2 3.2B Q4_K_M'],['Parâmetros','Temperatura 0 · contexto 8192 · JSON'],['Bateria','12 respostas; uma por caso/versão; sem retentativa'],['Controle','Configuração e digest conferidos antes/depois']],{h:390,widths:[290,870],size:25});
text(s,'Lote: 20261108T151915458937-provisional · dois pilotos separados.',64,593,1150,54,23);
s=slide('Ciclo de vida e evidências',3);
lines(s,['Objetivo GQM → A → mudança B → execução → avaliação → decisão.','Cada caso preserva request, resposta, mensagens do modelo e log.','Manifestos ligam código, prompt, digest, fonte e resultados.','Snapshot e hashes preservam o código usado antes do commit.'],160,28,104);
text(s,'Condições reconstruíveis; igualdade exata das gerações não é garantida.',64,600,1150,45,24,navy,true);
s=slide('Rubrica e avaliação humana prevista',4);
table(s,[['Dimensão','0','1','2'],['Correção','Erro substantivo','Parcial / erro menor','Sem erro identificado'],['Relevância','Não atende','Atende parcialmente','Atende à tarefa'],['Suporte','Sem apoio','Apoio parcial','Sustentado / abstenção justificada']],{h:330,widths:[220,280,300,360],size:23});
text(s,'Aprovação: 2/2/2 e nenhuma falha crítica. R1: 12 notas; R2: CT01/CT05 A/B (4).',64,535,1150,90,27);
s=slide('Estado das avaliações e do lote',4);
lines(s,['Referências ainda sem revisão humana prévia: lote provisório.','R1 e R2: formulários em branco, para avaliações independentes.','Pareceres complementares aplicados por Codex, identificados como IA.','Notas humanas, consenso e concordâncias humanas: pendentes.'],160,28,104);
text(s,'A origem do parecer faz parte da integridade do experimento.',64,600,1150,45,24,red,true);
s=slide('Tabela das 12 respostas',5);
for(const [idx,v] of ['A','B'].entries()){
 text(s,`Versão ${v}`,65+idx*590,145,550,40,27,navy,true);
 const vals=data.rows.filter(r=>r.version===v).map(r=>[r.case_id,r.f1.toFixed(3),r.automatic_approved?'Aprova':'Reprova',`${r.correcao}/${r.relevancia}/${r.suporte}`]);
 table(s,[['Caso','F1','Auto','C/R/S IA'],...vals],{x:60+idx*590,y:195,w:570,h:375,size:22,widths:[110,110,150,200]});
}
text(s,'Notas C/R/S são da IA. Aprovação integral pela rubrica IA: 0/6 em A e 0/6 em B.',64,600,1150,50,24,red);
s=slide('F1 lexical por caso',5);
const chart=s.charts.add('bar',{position:{left:70,top:155,width:1140,height:405},categories:['CT01','CT02','CT03','CT04','CT05','CT06'],series:['A','B'].map((v,i)=>({name:`Versão ${v}`,values:data.rows.filter(r=>r.version===v).map(r=>Number(r.f1.toFixed(6))),fill:i?red:navy})),barOptions:{direction:'column',grouping:'clustered'},hasLegend:true,legend:{position:'bottom',textStyle:{fontSize:20}},yAxis:{min:0,max:1,majorUnit:.25,numberFormatCode:'0.00',textStyle:{fontSize:18}},xAxis:{textStyle:{fontSize:20}},dataLabels:{showValue:true,position:'outEnd',numberFormatCode:'0.00',textStyle:{fontSize:17}},chartFill:'#FFFFFF'});
applyPresentationChartFont(chart,{fontFamily:'Arial'});
text(s,`F1 médio: A=${data.metrics.versions.A.mean_f1.toFixed(3)}; B=${data.metrics.versions.B.mean_f1.toFixed(3)}. Tau=0,5 → 5/6 aprovadas em cada versão.`,64,583,1150,70,27);
s=slide('Um erro factual com F1 alto',6);
text(s,'CT02/B · F1 = 0,857 · sinal automático aprova',64,160,1150,58,34,navy,true);
table(s,[['Fonte','Resposta de B'],['Produto Dália: R$ 0.00','preco_brl: null']],{y:250,h:180,widths:[580,580],size:30});
text(s,'Zero era um preço conhecido. Chaves e termos semelhantes mantiveram o F1 alto.',64,475,1150,95,30);
text(s,'Outro caso: CT06/B teve F1=0,800 e perdeu os dois preços sob paráfrase.',64,600,1150,58,25,red);
s=slide('Interpretação e decisão',6);
lines(s,['Auto–IA: 2/12 decisões iguais; dez diferenças explicadas nas evidências.','B não corrigiu os trechos e introduziu perdas factuais em CT02/CT06.','Recomendação técnica da IA: revisar B antes de avançar.','Decisão experimental final: aguarda notas humanas e revisão das referências.'],160,28,104);
s=slide('Limitações e acompanhamento',7);
lines(s,['Seis casos sintéticos; CT06 é relacionado a CT01; uma execução por condição.','Pareceres IA não medem concordância entre pessoas. Cegamento limitado.','Acompanhar erro factual, abstenção indevida e apoio insuficiente.','Voltar ao prompt A se surgir regressão, preservando B e os registros.'],160,28,104);
s=slide('Materiais e próximos passos',7);
lines(s,['Repositório organizado em atividade2/ e atividade3/.','Concluir revisão humana, decisão, contribuições e conferência dos materiais.','Vídeo: pasta informada pela equipe e vinculada no README, relatório e VIDEO.md.','Entrega: 11/11. Apresentação: 12/11, 10–12 min + 3–5 min de perguntas.'],160,27,100);
text(s,'Uso de IA declarado: apoio de Codex; modelo estudado: llama3.2.',64,594,1150,55,24,navy,true);
s.speakerNotes.text += ` Vídeo fornecido pela equipe: ${data.video}. Reprodução e participação integral não verificadas.`;
await fs.writeFile(path.join(base,'apresentacao/slide-order.json'),JSON.stringify(outline,null,2));
for(const [i,sl] of p.slides.items.entries()){
 const png=await p.export({slide:sl,format:'png',scale:1});await fs.writeFile(path.join(build,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
const candidate=path.join(build,'candidate.pptx');await(await PresentationFile.exportPptx(p)).save(candidate);
const final=path.join(base,'apresentacao/slides_av3.pptx');
const result=await finalizePresentation({workspaceDir:base,candidatePath:candidate,finalPath:final,pythonExecutable:path.join(runtime,'python/python.exe'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...[3,4,7,9,11,13].flatMap(n=>['--require-native-table-slide',String(n)])],requiredNativeTableOwnerSlides:[3,4,7,9,11,13],requiredNativeChartOwnerSlides:[12],explicitTotalSlideCount:16,fontPolicy:{basis:'design',families:['Arial']},materializeLiteralChartWorkbooks:true,verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')});
console.log(JSON.stringify(result));
