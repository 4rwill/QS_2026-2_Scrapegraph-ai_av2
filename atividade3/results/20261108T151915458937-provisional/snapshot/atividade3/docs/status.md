# Status AV3 — 07/11/2026

**Viável com o projeto existente. Iniciada; ainda não concluída ou submetida.** A revisão humana das referências é o próximo requisito obrigatório antes da bateria final. A promessa de revisão futura da equipe foi registrada em manual-checklist.md; não é confirmação de revisão realizada.

## Etapas e evidências

| Etapa / requisito | Estado | Evidência | Bloqueio / próximo passo | Responsável |
|---|---|---|---|---|
| Ler quatro páginas e comparar requisitos com AV2 | verificado | enunciado-extraido.txt, enunciado-origem.json | Nenhum; recorte preservado em atividade3/ | Codex |
| GQM: objetivo, duas perguntas e três medidas | implementado | protocol.md | Conferência humana proposta antes da bateria | Eduardo Curcino, proposto |
| Seis casos, fontes e referências | implementado | ../data/cases.json, cinco HTMLs | Referências precisam ser revisadas por pessoa | Arthur / Artur José, propostos |
| Versões A/B e manifestos | implementado | ../versions/, ../config.json | Única mudança principal: prompt | Codex; equipe revisa |
| Ambiente reutilizado | verificado | ../results/20261107T234217513508-check.json | Ollama iniciado; mesmo digest/modelo/commit | Codex |
| Executor, F1, planilhas e consolidação | implementado | ../scripts/, ../tests/ | Consolidação real depende de anotações humanas | Codex |
| Pilotos reais CT01/A | executado | ../results/20261107T234218278552-pilot/ e ../results/20261107T234557389615-pilot/ | Duas verificações de infraestrutura, ambas excluídas das 12 finais | Codex |
| Bateria final de 12 saídas | bloqueado | reference-review.csv ainda pendente | Registrar revisão humana real das seis referências | Equipe, depois executor |
| 12 avaliações R1 + quatro R2 | manual | Pacotes gerados após bateria; rubrica pronta | Fazer independentemente; registrar nomes/notas/justificativas | Christian / Artur José, propostos |
| Consenso, métricas humanas, divergência e decisão | pendente | analyze.py e regra protocol.md | Necessita notas reais; indisponível não equivale a zero | Equipe e Codex |
| Relatório, roteiro de apresentação e tarefas | implementado como rascunho | report.md, presentation-plan.md, manual-checklist.md | Completar com resultados e contribuições reais | Equipe |
| PDF, slides, vídeo e submissão | manual | ../VIDEO.md | Entrega 11/11; apresentação 12/11 | Equipe |

## Verificações e reprodução

Na raiz do repositório:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s atividade3/tests -v
.\.venv\Scripts\python.exe atividade3/scripts/experiment.py check
```

O piloto foi executado com `experiment.py pilot`: uma resposta real, configuração correspondente ao plano, mensagens do modelo e saída preservadas. O modelo retornou Aurora=10 e Cedro=20, com trechos contendo apenas os preços. Essa inspeção não é anotação humana nem comparação A/B. Tempo registrado do grafo: cerca de 19,07 s; não é avaliação de desempenho em produção.

Na primeira verificação dos testes, dois controles falharam por permissão do Windows em diretórios temporários privados (`tempfile`), inclusive no workspace. Foi ajustada a criação dos temporários dos testes; a lógica de pontuação permaneceu igual. Nove controles passaram após esse ajuste; depois foi acrescentado um controle integrado de pacotes/consolidação. Resultado final e log ficam em `results/verification.json` e `results/verification-tests.log`. Esses testes usam dados sintéticos conhecidos; não contam como saídas do modelo nem anotações humanas.

Após o primeiro piloto, o executor foi reforçado para ler worker/prompts/fontes diretamente da cópia congelada de cada execução. O segundo piloto verificou esse caminho e também produziu uma resposta com configuração correspondente. Ambos preservam o código realmente usado e não integram a bateria final. A integração de formulários e métricas passou no décimo controle sintético, incluindo os denominadores 12 e 4 e a preservação das notas originais. Hash do texto da fonte também foi vinculado a cada caso/revisão antes da bateria final.

`experiment.py final` recusa executar enquanto uma referência estiver sem aprovação humana ou com hash divergente. O bloqueio é metodológico (parte B do enunciado: referência curta revisada por pessoa), não falta de instalação. Não se preenche aprovação em nome dos integrantes.

## Reaproveitamento e preservação

Verificação final desta etapa: dez controles passaram, conforme `results/20261107T234728-verification.json` e log associado (caminhos relativos à pasta atividade3). Os 12 links locais dos documentos foram conferidos; os snapshots dos dois pilotos mantêm seus hashes e cada piloto capturou uma chamada ao modelo. A tentativa de `experiment.py final` recusou corretamente a execução por revisão pendente, sem criar lote final. Não há métricas humanas calculadas.

Repositório AV2 em `C:/Projetos/QS_2026-2_Scrapegraph-ai_Atividade2`, base `9f9ea26d0c33510b2c486a017445b38e1a8c1e9f`. Sistema estudado em `Scrapegraph-ai`, commit `194055e203afce41ed4e70365dbc416bad756115`, limpo na inspeção. Clones e relatório AV2 não foram alterados. Alterações preexistentes de roteiro, output e tmp foram preservadas.

Apenas a ligação para a AV3 foi acrescentada ao README principal; atributos Git preservam os bytes das novas evidências. Não houve commit, push ou submissão nesta etapa. Horário final da entrega não consta no PDF AV3 e precisa ser consultado pela equipe no Classroom. A autorização da equipe de oito na AV2 permanece registrada; AV3 pede manter a equipe.
