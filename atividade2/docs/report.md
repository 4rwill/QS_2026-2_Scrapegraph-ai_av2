> Rascunho histórico de 10/10/2026, desatualizado. O relatório atual é relatorio/relatorio_av2.tex. Auditoria e contribuições foram confirmadas em 15/10/2026 conforme docs/review-confirmation.md. Não usar os bloqueios e pendências abaixo como estado atual.

# Relatório técnico AV2 - RASCUNHO, NÃO SUBMETER

## Identificação e recorte
Equipe 08, oito integrantes conforme usuário. Instituição, docente, composição nominal AV2 e autorização excepcional para oito: pendentes. Entrega prevista no enunciado: 21/10/2026 às 23h59, fuso/canal a confirmar. Apresentação em 22/10, 10–12 minutos e perguntas 3–5 minutos. Vídeo: URL PENDENTE.

Missão C proposta: extração estruturada confiável por SmartScraperGraph de catálogo sintético local, com resistência à injeção e auditoria de trechos. Justificativa: retoma AV1, oferece gabarito observável e evita dependência de coleta externa/API paga. A equipe precisa validar a missão.

## Ficha e fluxo
ScrapeGraphAI, MIT, versão 2.3.1, commit 194055e203afce41ed4e70365dbc416bad756115. AV1 usou 2.2.4, commit c75c8084fae2d4f5ba01a8c218bc1168b67e3569. Não atribuir diferenças de versão à melhoria de prompt.
Usuário fornece tarefa e schema. FetchNode recebe HTML local. GenerateAnswerNode usa Ollama solicitado llama3.2:latest com temperatura 0 e contexto 8192. JSON segue para validador local e logs. html_mode=true, sem busca RAG, ações externas, reasoning ou retry. Fontes sintéticas identificadas no manifesto SHA-256. Digest/versão de modelo real ainda indisponíveis.

## Histórico e limitações da AV1
README e evidências históricas registram 14 testes com 8 A, 3 P, 3 R e 15 repetições estáveis. ACH-01..06 descrevem contradições, string null, erro NA, exposição de token sintético, ranking sem critério e warning após timeout. Esses resultados pertencem à AV1. PDF disponível é preliminar e diverge dos registros posteriores de revisão e vídeo. Leitura detalhada em docs/av1-review.md.

## Prompts e metodologia
P1 direto, P2 estruturado, P3 com exemplos independentes. Mesma tarefa nas fontes correct e irrelevant gera seis combinações. Avaliar utilidade por extração/abstenção, fundamentação por manifesto e apoio do trecho, previsibilidade pelo formato. Não há vencedor observado.
Dez casos: três funcionais, dois de contexto/fontes, dois metamórficos, dois adversariais e um de saída. Esperados definidos em tests/cases.csv antes de chamadas. Máximo de 16 grafos por lote, 90 segundos por processo, sem retries. Metamórficos comparam CT-01. Contexto/prompt/saída e metadados ficam em lote imutável, sem editar dados brutos.

## Ameaças e controles
T1: injeção direta/indireta altera preço ou acrescenta ATAQUE_OK. T2: fonte/trecho inventado elimina proveniência. T3: JSON inválido ou tipo incorreto quebra consumidores. T4: infraestrutura ou ausência de logs gera conclusão não rastreável. Controles e requisitos ligados em threats.csv e improvement-plan.csv.

## Execução e evidências atuais
O avaliador foi executado com oito controles sintéticos aprovados: quatro condições obrigatórias negativas, controle positivo, string null, boolean como preço e duplicação. Não são respostas do ScrapeGraphAI.
Lote 20261010T152450-baseline registrou 16 solicitações como não executadas, nenhuma chamada ao modelo. Preflight inicial mostrou dependências ausentes e conexão Ollama recusada. Posteriormente, dependências foram instaladas na .venv e o import de SmartScraperGraph foi verificado. Versões registradas em results/evidence/dependencies.txt. Usuário confirmou que Ollama não está instalado; inferência real permanece bloqueada. Não afirmar funcionamento do grafo antes de execução real.

## Auditoria e métricas
Auditoria de 3–5 afirmações reais ainda bloqueada. Critério: primeiros fatos não nulos por ID, sem escolher somente acertos. Registrar afirmação, fonte, trecho, validade e veredito humano. Fonte acessível e apoio semântico são distintos. Precisão operacionalizada como apoio integral/citações verificadas, parciais separados.
Saídas reais=0; validade estruturada=indisponível (0 respostas); sucesso de injeção=indisponível (0 ataques executados); cobertura e precisão de citações=null. Não substituir indisponibilidade por zero. Métricas por lote em results/summary. Comparação qualitativa P1/P2/P3 e latências do modelo pendentes.

## Achados e melhorias
Três achados atuais documentam ambiente indisponível, mudança de versão e discrepância editorial histórica. Não são três falhas novas comprovadas do modelo. Plano: validador estrito com rejeição determinística, separação de conteúdo/instruções no P2 e abstenção diante de ausência/conflito. Implementação local do validador passou controles; efeito em respostas reais e retestes equivalentes estão pendentes. Baseline e melhoria devem usar mesmo digest, fontes e casos, guardando ambos.

## Limitações e continuidade
Um grafo, fontes sintéticas curtas, um modelo local proposto. Sem evidência de estabilidade AV2, robustez geral ou recuperação web. Apoio de trecho automatizado só verifica condições literais e gabarito; revisão humana continua obrigatória. Rodar preflight, selftest e lote após disponibilizar dependências/modelo; auditar 3–5 afirmações e consolidar métricas antes da versão final.

## Entrega, contribuições e referências
URL do vídeo: PENDENTE. Participação, gravação, hospedagem, ensaio, apresentação e submissão não realizados nesta sessão. Contribuições AV2 a registrar em docs/contributions.md. Codex preparou protocolo, código e rascunhos; equipe revisa e confirma resultados, conforme regras institucionais a consultar.
Referências efetivamente consultadas: enunciado AV2 local (hash em results/evidence/enunciado-origem.json); C:/Projetos/AGENTS.md; Scrapegraph-ai/AGENTS.md, pyproject.toml, SmartScraperGraph, FetchNode e GenerateAnswerNode; clone AV1 README, metodologia, contribuições, ACH-01..06 e PDF preliminar (hash registrado). Não foram consultadas novas fontes externas para fundamentar resultados.
