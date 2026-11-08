# Rubrica

| Dimensão | 0 | 1 | 2 |
|---|---|---|---|
| Correção | Erro substantivo, produto/preço inventado ou saída inutilizável | Parcial/erro menor | Sem erro identificado ao conferir fonte e referência |
| Relevância | Não atende à extração | Atende parcialmente | Atende, inclusive abstenção correta |
| Suporte | Sem apoio na fonte | Apoio parcial ou trecho insuficiente | Afirmações sustentadas e trecho identificável, ou abstenção justificada |

Falha crítica=1 se inventar produto/preço, escolher preço vigente sem evidência em conflito, atribuir fonte inexistente ou não produzir saída utilizável (falha/vazia). Nos demais casos 0, sem dispensar a rubrica. Ausência de preço com produto existente pede `null`, não apagar produto. Sem catálogo: produtos vazios e motivo explicativo. Não exigir igualdade literal do motivo para nota humana. O trecho deve ligar nome ao preço; em conflito, registrar evidência do conflito, sem escolher um valor.

R1 avalia 12 saídas; R2 avalia CT01 e CT05 de A/B (quatro), sem consultar notas de R1. Pacotes separados ocultam versão e F1; quem executou ou leu resultados pode reconhecer variantes. Registrar exposição e outras limitações do cegamento. Não discutir antes de salvar as notas individuais. Para diferenças, preencher consenso separado com justificativa, preservando originais. Ausência de anotações = indisponível, nunca zero.

