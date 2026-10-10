# Status AV2 - 10/10/2026, America/Sao_Paulo

Não entregue. Missão C aprovada pelo usuário. Equipe com 8 e confirmação presencial com professor declaradas pelo usuário; detalhes de canal/fuso não transcritos. Clones preservados. Ollama portátil 0.40.2 instalado, assinatura válida; modelo llama3.2 instalado e preflight aprovado; execuções reais concluídas. Resultados dos lotes anteriores continuam não executados. Documento, slides e vídeo serão feitos pelo usuário.

| Etapa | Requisito | Estado | Evidência | Bloqueio | Próximo passo | Responsável |
|---|---|---|---|---|---|---|
| 1 | Inventário, enunciado e AV1 | verificado | repositories.md, av1-review.md, results/evidence/*-origem.json e *-texto.txt | PDF histórico preliminar | manter histórico separado | Codex; equipe revisa |
| 2 | Missão/ficha/requisitos | implementado | mission.md, system-card.md | validação do recorte | equipe confirmar missão C | equipe |
| 3 | Ambiente e avaliador | implementado | .venv, scripts/evaluate.py, preflight-20261010T152807.json, selftest*.json | Ollama/modelo ausentes | instalar/disponibilizar Ollama; repetir preflight | ambiente a confirmar |
| 4 | Três prompts × duas condições | bloqueado | prompts/, seis requests LAB em results/raw/20261010T152450-baseline | sem modelo | executar lote real | Codex após ambiente |
| 5 | Ameaças e dez casos | verificado | threats.csv, tests/cases.csv, methodology.md | nenhum para plano | revisar critérios congelados | equipe |
| 6 | Execuções reais | bloqueado | results/summary/20261010T152450-baseline/results.csv | 16 registros não executados, 0 respostas | executar lote com Ollama | ambiente/Codex |
| 7 | Auditoria e saída | implementado | audit.csv, audit_metrics.py, selftest.json | 3–5 afirmações reais ausentes | preencher auditoria com respostas reais | revisores |
| 8 | Métricas, achados, melhorias/reteste | implementado | metrics.json, findings.csv, improvement-plan.csv | métricas do sistema null; retestes reais pendentes | auditar/calcular/comparar lotes | equipe/Codex |
| 9 | Relatório e reprodução | implementado | report.md, README, deliverables/relatorio-av2-rascunho.pdf | resultados/identificação/vídeo/acesso pendentes | completar e regenerar PDF | editor a confirmar |
| 10 | Slides/roteiro/checklist | implementado | presentation.md, video-script.md, PDF de slides, manual-checklist.md | tarefas humanas não realizadas | revisar, gravar, hospedar, ensaiar | oito integrantes |
| 11 | Conferência final | pendente | scripts/check_artifacts.py, lista abaixo | requisitos reais ainda incompletos | revisão final antes da submissão | representante |

## Reprodução e verificação da primeira preparação (histórico)

Raiz: C:/Projetos/QS_2026-2_Scrapegraph-ai_Atividade2. Python das verificações iniciais: C:/Users/chris/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe. Depois da instalação, `.venv/Scripts/python.exe` também executou preflight e selftest. Cada rodada grava arquivo novo; dados brutos não são editados.

1. Git status/remote/branch/rev-parse dos dois clones conforme repositories.md. PDFs lidos integralmente por pypdf e texto/hash guardados. Nenhum resultado histórico reclassificado como AV2.
2. Conferir mission.md/system-card.md e RQ-FUN/CTX/CIT/FMT/SEC/MET. Recorte provisório com critério objetivo por gabarito.
3. `.venv/Scripts/python.exe scripts/evaluate.py preflight`; `.venv/Scripts/python.exe scripts/evaluate.py selftest`. Oito controles passaram nos dois ambientes. `from scrapegraphai.graphs import SmartScraperGraph` importou com sucesso na .venv. Criação de venv falhou em ensurepip; instalação via pip do runtime com `--python .venv/Scripts/python.exe install -e ./Scrapegraph-ai` terminou com sucesso após autorização de escalonamento. Não pressupor pip instalado dentro da .venv; usar runtime externo para gerenciar pacotes. Versões congeladas em results/evidence/dependencies.txt.
4–6. `.venv/Scripts/python.exe scripts/evaluate.py run --limit 16`. Comando verificado no caminho bloqueado, não no caminho real. Se preflight falhar, não chama modelo e registra não executado. Instalar Ollama/modelo: procedimento pendente, não realizado. Máximo 16 grafos/lote, timeout 90s, sem retries. Modelo latest exige conferir digest.
7. `.venv/Scripts/python.exe scripts/audit_metrics.py`. CSV sem amostra gera denominador zero e ratio null. Automatização literal não substitui avaliação humana do apoio.
8. Métricas estruturais/injeção por lote geradas pelo run; leitura em results/summary. `run --variant improved` é comando preparado, ainda não executado: rejeita saída reprovada pelo adaptador; não corrige LLM. P2 e validador implementados; melhoria de sistema/reteste real não comprovados.
9–10. Runtime Python: `scripts/build_materials.py`, comando verificado. PDF relatório com 2 páginas e apresentação com 9 slides foram renderizados pelo Poppler e revisados visualmente. PNGs em deliverables. Fonte dos rascunhos indica resultados pendentes. Skill PDF e Presentations usadas. Regenerar após resultados e URL. Layout atual legível; revisão humana final pendente.
11. `.venv/Scripts/python.exe scripts/check_artifacts.py`: passou, verificando hashes, distribuição planejada, arquivos e clones limpos. Todos os scripts passaram análise sintática por ast.parse. Não verifica cumprimento acadêmico das execuções. Nova rodada com dependências instaladas: results/raw/20261010T152945-baseline e results/summary/20261010T152945-baseline, 16 registros não executados, 0 respostas, Ollama ausente. Os dois lotes foram preservados. Os PDFs foram regenerados após atualização do ambiente e revisados novamente.

## Gates da primeira preparação (histórico; ver estado consolidado abaixo)

- Instalar/disponibilizar Ollama e modelo; registrar versão/digest e primeira execução real. Caminho worker/callback/schema não validado com inferência real.
- Executar seis combinações e dez casos, preservar falhas, registrar prompts internos/calls e comparar metamórficos com referência real.
- Auditar 3–5 afirmações, consolidar contagens e qualificar três achados sustentados por dados. Nenhuma falha deve ser inventada para completar a quota.
- Validar missão, composição nominal, contribuições, docente/instituição e autorização para oito; confirmar fuso/canal.
- Gravar/hospedar vídeo, inserir URL nos três locais, revisar PDFs, tornar repositório acessível, ensaiar e submeter. Somente comprovantes humanos encerram essas tarefas.

## Continuação autorizada em 10/10/2026
Missão aprovada e confirmação presencial registradas em decisions.md. Ollama oficial 0.40.2 portátil instalado em .tools/ollama. Assinatura Authenticode válida. Iniciar: `powershell -File scripts/start_ollama.ps1`; baixar: `.tools/ollama/ollama.exe pull llama3.2:latest`. Modelo em download; serviço somente loopback. Fonte oficial: https://github.com/ollama/ollama/releases/tag/v0.40.2.

Ambiente verificado: preflight-20261010T175909.json, Ollama 0.40.2, modelo digest a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72. GPU GTX 1650. Execução real iniciada com limit 16, sem retentativas automáticas.

## Estado consolidado após execuções reais
Esta seção prevalece sobre os bloqueios históricos da primeira preparação.

| Etapa | Estado atual | Evidência | Próximo passo/responsável |
|---|---|---|---|
| 2 Recorte | verificado | mission.md; decisions.md, autorização do usuário | nomes/contribuições pela equipe |
| 3 Ambiente | verificado | preflight-20261010T175909.json; modelo e assinatura | reiniciar serviço quando necessário |
| 4 Prompts | executado | 6 LAB em 20261010T175910-baseline | revisar comparação; sem vencedor global |
| 5 Plano | verificado | ameaças e 10 casos | atualizar se novo recorte |
| 6 Testes | executado | 10 CT, respostas integrais e CSV do lote | validar julgamento com equipe |
| 7 Auditoria | executado | audit.csv, audit-metrics.json, 5 afirmações técnicas | revisão humana pendente |
| 8 Métricas/melhoria | executado | metrics.json, adapter-retest.json, results-analysis.md | melhoria gerativa ainda proposta |
| 9 Documento | manual | resultados prontos; usuário fará documento | atualizar com achados novos |
| 10 Slides/vídeo | manual | usuário fará materiais | gravação/hospedagem/ensaio pendentes |
| 11 Final | pendente | requisitos técnicos com evidências | revisão humana, links e submissão |

16/16 respostas reais, schema 16/16, ataque 1/2 bem-sucedido; CT completos: 0 aprovados, 8 reprovados, 2 inconclusivos. Os inconclusivos metamórficos dependem de referência reprovada no critério integral. Auditoria técnica: 5/5 fontes válidas, 4/5 afirmações integralmente sustentadas; revisão humana pendente. Trecho curto é problema distinto de fato errado. Reteste offline do adaptador sobre respostas reais libera 1/16; não é nova inferência nem correção do LLM. Três achados novos em results-analysis.md.

Reprodução verificada: iniciar scripts/start_ollama.ps1; preflight; selftest; evaluate.py run --limit 16; summarize_real_run.py; audit_metrics.py; check_artifacts.py. Avaliador captura mensagens internas e respostas brutas via callback. Lotes anteriores continuam preservados. PDF/slides rascunhos anteriores estão desatualizados; usuário fará os finais conforme results-analysis.md.

## Publicação do trabalho em andamento
Repositório de destino autorizado: https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2.git. Publicação técnica em preparação; não representa entrega acadêmica. Clones, runtime/modelo e rascunhos PDF/PNG ficam locais. README inclui reprodução em nova máquina com limitações explícitas.
