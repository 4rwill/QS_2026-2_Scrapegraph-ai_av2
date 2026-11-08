# AV3 — Métrica automática versus avaliação humana

**Rascunho metodológico; não é relatório de resultados concluídos.**

Universidade Federal de Sergipe — Departamento de Computação. Qualidade de Software, 2026.2. Prof. Dr. Glauco de Figueiredo Carneiro. Equipe 08. Identificação reaproveitada da AV2; curso/turma não informados.

Integrantes: Christian Will Silva Santos Nunes; Arthur Soares Santana; Artur José Soares Santos; Eduardo Curcino Monteiro Filho; Eduardo Ferreira Bomfim Filho; Iuri Maurício Maia Pereira; Pedro César Figueiredo Carneiro; Rian Purificação de Oliveira. Contribuições AV3: pendentes de realização/confirmação; consultar a distribuição proposta em manual-checklist.md.

## Recorte e hipótese

A AV2 mostrou que JSON válido não garante apoio factual. O novo experimento mantém o fluxo SmartScraperGraph com catálogo HTML sintético e testa se instruções adicionais de apoio literal e abstenção melhoram o julgamento humano. A usa o P2 anterior; B muda somente o prompt. Não se compara diretamente percentuais das atividades, pois casos e critérios mudaram. Não há reconstrução da aplicação ou treinamento.

## GQM e método

O objetivo, as duas perguntas, as três medidas, a rubrica e o critério de decisão estão em [protocol.md](protocol.md), registrados antes da bateria final. São quatro casos funcionais, um sem evidência suficiente e uma paráfrase de CT01. Referências propostas foram construídas diretamente das fontes; falta revisão por pessoa antes do teste final.

O desenho prevê seis casos por duas versões, uma execução por combinação. Modelo llama3.2 local via Ollama, temperatura zero, contexto 8192; demais condições fixas. F1 lexical usa o JSON serializado com chaves ordenadas, NFC, casefold, tokens Unicode de palavras e multiconjuntos. Tau=0,5. As chaves e a repetição de termos podem aumentar o score sem garantir fatos corretos.

Uma pessoa R1 avaliará 12 respostas; R2 avaliará CT01 e CT05 nas duas versões, independentemente. Aprovação exige notas 2 em correção, relevância e suporte, sem falha crítica. Diferenças exigem consenso separado. Nas demais oito saídas, vale R1, com essa limitação declarada.

## Resultados e visualização

**Bateria final: pendente. Notas humanas: pendentes.** Piloto é verificação de infraestrutura e não integra as 12 saídas. Não há conclusão sobre ganho de B, aprovação humana ou concordância.

Após execução e notas reais, inserir `consolidated.csv`, métricas por versão (denominador 6), concordância automático–humano (12) e R1–R2 antes do consenso (4). `comparison.html` fornece tabela e barras de F1. Tratar erros/vazios conforme protocolo sem removê-los do denominador.

## Divergência ou caso-limite

Pendente de notas reais. Selecionar pelo menos uma diferença entre sinal automático e decisão humana e citar saída, referência, fonte e justificativa. Se não existir diferença, declarar isso e discutir um caso-limite observado. O teste unitário de preço incorreto com F1 alto é apenas controle sintético do avaliador, não uma divergência humana observada.

## Versionamento e decisão

Diagrama e regras em protocol.md. Manifestos de cada execução ligarão prompt, código, configuração/modelo, casos/fontes, referências, saídas e notas. Hashes e cópia dos arquivos registram alterações locais ainda sem commit. Promover B só com ganho de aprovação humana e sem falha crítica/regressão; caso contrário manter A ou revisar, conforme regra anterior aos testes. Decisão atual: pendente.

## Limitações

Seis casos, CT06 relacionado a CT01, uma execução por condição, apenas quatro revisões duplas. Sintéticos não representam produção. Temperatura zero não garante estabilidade. Cegamento depende de não consultar scores/mapeamento e do conhecimento prévio dos avaliadores, a registrar nos formulários. JSON lexical contém termos de estrutura que não comprovam adequação. Não se ajusta tau após resultados.

## Uso de IA

Codex, modelo identificado pela sessão como GPT-6, apoiou leitura do enunciado, proposta GQM, referências preliminares, scripts e documentação. Não realizou avaliação humana. Prompt do usuário: “analise se é possível a realização da atividade 3 baseado no que já fizemos e se for possível já comece a fazer”. Uma sugestão aproveitada foi reaproveitar o worker AV2 preservando configuração e capturando evidências; a verificação está nos testes do avaliador e piloto registrados em status.md. Outra decisão foi manter revisões futuras como pendentes, sem notas atribuídas aos integrantes. Revisão dessa declaração pela equipe: pendente.

## Materiais e referências

Repositório-base: https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2 . Pasta local `atividade3/`; publicação dos novos arquivos ainda não realizada. Vídeo AV3: pendente (não reutilizar URL AV2).

Fonte efetivamente consultada: enunciado Atividade 3 revisado, quatro páginas; texto em enunciado-extraido.txt e origem/hash em enunciado-origem.json. Fontes técnicas efetivamente consultadas: código `scripts/evaluate.py`, P2, fixtures e evidências AV2 do lote 20261010T175910-baseline. As referências GQM/NIST/JUDGE indicadas no enunciado são leituras de partida; não foram consultadas nesta etapa e não são apresentadas como lidas.


## Relatório atual — 08/11/2026

O fonte atual está em [relatorio_av3.tex](../relatorio/relatorio_av3.tex). A bateria de 12 respostas foi executada como provisória; F1 e rubrica IA foram consolidados. Avaliações humanas permanecem pendentes. A descrição inicial acima é histórica. Vídeo AV3: https://drive.google.com/drive/folders/1ln8dIKPjHpep5eWkHJ-mPIhnB0MO94QZ?usp=sharing .
