# Atividade 3 · Métricas automáticas e avaliação de respostas

**Equipe 08 · UFS · Qualidade de Software · 2026.2**

Comparação de dois prompts do SmartScraperGraph nos mesmos seis casos sintéticos. A usa P2 da AV2; B acrescenta instruções para apoio literal, preço ausente, conflito e abstenção. Modelo, fontes, schema e parâmetros foram mantidos.

[Relatório LaTeX](relatorio/relatorio_av3.tex) · [Slides PPTX](apresentacao/slides_av3.pptx) · [Slides Beamer](apresentacao/slides_av3.tex) · [Roteiro](apresentacao/roteiro_apresentacao.md) · [Vídeo](https://drive.google.com/drive/folders/1ln8dIKPjHpep5eWkHJ-mPIhnB0MO94QZ?usp=sharing)

## Resultados registrados

Lote [20261108T151915458937-provisional](results/20261108T151915458937-provisional), executado em **08/11/2026**. Foram 12 respostas, uma chamada por caso/versão, sem retentativa e com configurações correspondentes ao plano.

| Indicador | A | B |
|---|---:|---:|
| Respostas | 6/6 | 6/6 |
| F1 lexical médio | 0,748 | 0,701 |
| Sinal automático aprovado, tau=0,5 | 5/6 | 5/6 |
| Aprovação integral da rubrica **por IA** | 0/6 | 0/6 |
| Aprovação humana | Pendente | Pendente |

**Caso ilustrativo:** CT02/B recebeu F1=0,857, mas substituiu o preço conhecido zero por null. Em CT06/B, os dois preços explícitos viraram null sob paráfrase. Sobreposição lexical não verifica esses fatos.

A rubrica foi aplicada por Codex como análise adicional, com origem explícita. A concordância automático–IA foi **2/12**; concordância automático–humano e R1–R2 estão indisponíveis. Há [tabela consolidada e justificativas](results/20261108T151915458937-provisional/ai-analysis-20261108T152247707442/consolidated.csv).

## Estado metodológico

O lote é **completo provisório**: a revisão humana das referências ainda não ocorreu. O protocolo registra esse desvio antes das chamadas. As 12 avaliações R1 e quatro R2 continuam em branco nos pacotes do lote. Uma releitura pelo mesmo assistente não equivale a uma segunda pessoa independente.

Recomendação técnica da IA: revisar B antes de avançar. **Decisão experimental humana: pendente.** Resolver a aceitação do lote provisório e completar avaliações reais antes de declarar conclusão acadêmica.

## Materiais e reprodução

| Material | Acesso |
|---|---|
| Plano GQM, rubrica e regra de decisão | [Protocolo](docs/protocol.md) |
| Seis perguntas/referências e fontes | [Casos](data/cases.json) · [Guia de revisão](docs/reference-review.md) |
| Prompts e manifestos | [A](versions/A) · [B](versions/B) · [Manifestos efetivos no lote](results/20261108T151915458937-provisional) |
| Execução e consolidação | [Scripts](scripts/) · [Reprodução](docs/reproduction.md) |
| Relatório e apresentação | [Relatório](relatorio/relatorio_av3.tex) · [16 slides](apresentacao/slides_av3.pptx) · [Beamer](apresentacao/slides_av3.tex) · [Roteiro de oito blocos](apresentacao/roteiro_apresentacao.md) |
| Pendências e responsáveis propostos | [Status](docs/status.md) · [Checklist](docs/manual-checklist.md) |
| Vídeo AV3 | [Pasta da equipe](https://drive.google.com/drive/folders/1ln8dIKPjHpep5eWkHJ-mPIhnB0MO94QZ?usp=sharing) · [Estado da conferência](VIDEO.md) |

Os fontes LaTeX seguem a identificação e a formatação da AV2. A compilação integrada foi bloqueada pelo Windows antes de executar o compilador; nenhum PDF foi verificado. O PPTX foi renderizado e validado estruturalmente, com tabelas e gráfico editáveis. Abertura no PowerPoint da equipe e duração de ensaio ainda precisam ser conferidas.

Entrega: **11/11/2026**. Apresentação: **12/11/2026**, 10–12 minutos e 3–5 minutos de perguntas. O link do vídeo foi informado pela equipe; reprodução integral e participação de todos ainda não conferidas. Não há comprovação de submissão.
