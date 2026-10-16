# Reconferência técnica da auditoria - 15/10/2026

Responsável técnico: Codex. Validação humana realizada segundo confirmação do representante em 15/10/2026, sem divergências, incluindo Christian Will Silva Santos Nunes na auditoria e Artur José Soares Santos no conflito. Registro em review-confirmation.md. Nenhuma resposta nova foi gerada e nenhum dado bruto foi alterado.

Lote results/raw/20261010T175910-baseline. Critério mantido: primeiros cinco fatos de preço não nulo por ID. Comparados request.json, response.json, fixtures e data/manifest.json. Os hashes das três fontes coincidiram; contextos correspondem às fontes com normalização de quebras de linha na leitura textual.

| Linha de audit.csv | Afirmação | Evidência da resposta | Apoio na fonte | Veredito |
|---|---|---|---|---|
| 1 | Aurora: preço atual 10 | CT-01/response.json, produtos[0] | correct: Produto Aurora: R$ 10.00 | sustentada |
| 2 | Cedro: preço atual 20 | CT-01/response.json, produtos[1] | correct: Produto Cedro: R$ 20.00 | sustentada |
| 3 | Cedro: preço atual 20 | CT-03/response.json, produtos[0] | reordered: Produto Cedro: R$ 20.00 | sustentada |
| 4 | Aurora: preço atual 10 | CT-03/response.json, produtos[1] | reordered: Produto Aurora: R$ 10.00 | sustentada |
| 5 | Aurora: preço atual 10 | CT-05/response.json, produtos[0] | conflict: Aurora tem preços 10 e 99, sem indicação de vigente | parcialmente sustentada |

Os quatro primeiros fatos são sustentados pela fonte completa. O modelo emitiu apenas o preço como trecho, sem nome; por isso os casos continuam reprovados no contrato estrito do trecho. Audit.csv contém apoio encontrado pelo auditor, distinto do trecho emitido preservado em response.json. No quinto fato, 10 aparece na fonte, mas não pode ser afirmado como vigente; esperado null, apesar de a resposta reconhecer o conflito em motivo.

Cobertura de fontes locais: 5/5 = 100%; validade significa ID do manifesto e integridade da fonte, não disponibilidade de URL pública. Precisão na amostra: 4/5 = 80%; parcial: 1/5. Os denominadores são as cinco afirmações/citações selecionadas. Duas afirmações se repetem em fontes de ordem diferente; amostra pequena não estima precisão geral.

## Procedimento da conferência humana confirmada

1. Abrir respostas CT-01/03/05 e fixtures correct.html, reordered.html e conflict.html.
2. Conferir nome/preço, fonte indicada, trecho emitido e trecho completo encontrado pelo auditor.
3. Confirmar ou contestar cada veredito, registrando nome, data e divergências.
4. Registrar a confirmação posterior separadamente: audit.csv preserva o parecer técnico inicial; review-confirmation.md e human-review-2026-10-15.json documentam a declaração humana consolidada.

Reprodução na raiz AV2: `.venv/Scripts/python.exe scripts/audit_metrics.py` e `.venv/Scripts/python.exe scripts/check_artifacts.py`. Evitar executar summarize_real_run.py depois da revisão humana: ele regenera audit.csv com parecer técnico automático inicial.
