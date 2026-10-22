# ScrapeGraphAI · Missão Contexto Confiável

**Qualidade de Software · AV2 · Equipe 08 · UFS · 2026.2**

Avaliação do **SmartScraperGraph** na extração de nomes e preços de um catálogo HTML sintético. A missão **Saída Estruturada Confiável** investiga se uma resposta em JSON também é correta, fundamentada na fonte e resistente a instruções maliciosas.

[Relatório](relatorio/relatorio_av2.tex) · [Resultados](docs/results-analysis.md) · [Casos de teste](tests/cases.csv) · [Reprodução](docs/reproduction.md) · [Vídeo](https://drive.google.com/drive/folders/15KSnbY4aX-YjaW439icq2QOMwIBJHq0E?usp=sharing)

## O que foi avaliado

O sistema recebe uma instrução, o conteúdo HTML e um schema com os campos de saída. A resposta passa por verificações separadas de formato, valores e apoio na fonte.

```text
Prompt + HTML sintético + schema
              ↓
      SmartScraperGraph
       Ollama / llama3.2
              ↓
        Resposta JSON
              ↓
   Validação e evidências
```

O experimento inclui **três prompts em duas condições de contexto**, além de **dez casos**: três funcionais, dois de contexto/fontes, dois metamórficos, dois adversariais e um de saída estruturada. Foram usados somente dados sintéticos, sem ações sobre serviços de terceiros.

## Resultados reais disponíveis

Execução de **10/10/2026**, lote `20261010T175910-baseline`.

| Indicador | Resultado observado |
|---|---|
| Respostas reais | **16** — seis do laboratório e dez dos casos |
| Saídas válidas no schema | **16/16 (100%)** |
| Ataques bem-sucedidos | **1/2 (50%)** — o ataque direto alterou a resposta |
| Fontes válidas na amostra auditada | **5/5 (100%)** |
| Afirmações integralmente sustentadas na amostra | **4/5 (80%)** — uma parcialmente sustentada |

**JSON válido não garante conteúdo confiável.** No critério completo dos dez casos, houve oito reprovações e dois inconclusivos. Os metamórficos foram executados, mas ficaram inconclusivos pela dependência de uma referência reprovada. As métricas de citações consideram fontes locais e apoio na fonte completa, não apenas o trecho emitido.

O validador foi reaplicado **offline às respostas existentes**, liberando uma de 16. Esse reteste não representa novas inferências nem correção do modelo. A amostra é restrita; os resultados não demonstram robustez geral.

→ [Análise e limitações](docs/results-analysis.md) · [Evidências completas](results/raw/20261010T175910-baseline) · [CSV de resultados](results/summary/20261010T175910-baseline/results.csv)

## Materiais do trabalho

| Material | Acesso |
|---|---|
| Relatório em LaTeX | [Fonte](relatorio/relatorio_av2.tex) · [Orientações de compilação](relatorio/README.md) |
| Prompts e testes | [P1/P2/P3](prompts) · [Casos](tests/cases.csv) · [Schema](tests/schema.json) |
| Auditoria | [Cinco afirmações](docs/audit.csv) · [Revisão](docs/audit-review.md) |
| Segurança e melhoria | [Ameaças](docs/threats.csv) · [Achados](docs/findings.csv) · [Plano de melhoria](docs/improvement-plan.csv) |
| Equipe | [Contribuições](docs/contributions.md) · [Confirmação das revisões](docs/review-confirmation.md) |
| Vídeo | [Pasta do vídeo AV2](https://drive.google.com/drive/folders/15KSnbY4aX-YjaW439icq2QOMwIBJHq0E?usp=sharing) · [Informações](VIDEO.md) |

## Como reproduzir

O ambiente registrado utiliza **Python 3.12, ScrapeGraphAI 2.3.1, Ollama 0.40.2 e llama3.2**, com temperatura zero e contexto de 8192 tokens.

O [guia de reprodução](docs/reproduction.md) reúne instalação, versões, limites e comandos verificados. Para consultar os resultados salvos, não é necessário instalar o modelo.

## Situação da entrega

Testes e evidências disponíveis; auditoria e contribuições confirmadas pelo representante em **15/10/2026**, sem divergências. O vídeo foi disponibilizado pela equipe em **21/10/2026**. Faltam a disponibilização/conferência do PDF e dos slides finais e a revisão integral do vídeo. A submissão acadêmica não está registrada como concluída.

[Checklist de entrega](docs/manual-checklist.md) · [Histórico e status](docs/status.md)
