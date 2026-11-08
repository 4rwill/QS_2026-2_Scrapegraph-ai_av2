# Caminhos atuais após reorganização — 08/11/2026

A partir da raiz do repositório (ambientes e clones continuam nela):

```powershell
.\.venv\Scripts\python.exe atividade2/scripts/evaluate.py preflight
.\.venv\Scripts\python.exe atividade2/scripts/evaluate.py selftest
.\.venv\Scripts\python.exe atividade2/scripts/evaluate.py run --limit 16
.\.venv\Scripts\python.exe atividade2/scripts/audit_metrics.py
powershell -ExecutionPolicy Bypass -File atividade2/scripts/start_ollama.ps1
```

Não iniciar outro servidor se já estiver ativo. Novas execuções geram novos lotes e não substituem evidências anteriores. A avaliação sintética e as métricas da auditoria foram verificadas após a mudança de caminhos; a bateria histórica de 16 inferências não foi repetida apenas pela reorganização. O registro abaixo descreve a instalação e os comandos anteriores à separação das pastas; acrescentar atividade2/ aos caminhos de artefatos e scripts quando executar da raiz atual.

---

# Reprodução da avaliação

Este guia reúne instalação, configuração e comandos. Para consultar os resultados já registrados, não é necessário instalar o modelo: use a [análise](results-analysis.md) e as [evidências do lote](../results/raw/20261010T175910-baseline).

## Ambiente utilizado

| Componente | Registro |
|---|---|
| Python | 3.12.14 |
| ScrapeGraphAI | 2.3.1, commit `194055e203afce41ed4e70365dbc416bad756115` |
| Ollama | 0.40.2 |
| Modelo | `llama3.2:latest`, 3.2B, Q4_K_M |
| Temperatura | 0 |
| Contexto configurado | 8192 tokens |
| Lote de referência | `20261010T175910-baseline` |

Digest do modelo: `a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72`. A tag `latest` pode mudar; conferir o digest no preflight antes de comparar resultados. As [dependências observadas](../results/evidence/dependencies.txt) e o [ambiente do lote](../results/raw/20261010T175910-baseline/environment.json) complementam esse registro.

## Preparação em outra máquina

Pré-requisitos: Git, Python 3.12 e Ollama. Os comandos abaixo estão preparados para PowerShell. A instalação completa em máquina limpa ainda não foi verificada; os comandos de avaliação foram executados no ambiente registrado.

```powershell
git clone https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2.git
cd QS_2026-2_Scrapegraph-ai_av2

git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git Scrapegraph-ai
git -C Scrapegraph-ai checkout --detach 194055e203afce41ed4e70365dbc416bad756115

python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements-evaluation.txt
```

Instalar o Ollama pela [distribuição oficial](https://ollama.com/download), iniciar o serviço local e baixar o modelo:

```powershell
ollama pull llama3.2:latest
```

O serviço deve responder em `127.0.0.1:11434`. Se já estiver ativo, não iniciar outra instância. `scripts/start_ollama.ps1` serve apenas à instalação portátil em `.tools/ollama`, usada neste computador; o executável e o modelo não são versionados.

## Executar a avaliação

Na raiz do repositório:

```powershell
.venv/Scripts/python.exe scripts/evaluate.py preflight
.venv/Scripts/python.exe scripts/evaluate.py selftest
.venv/Scripts/python.exe scripts/check_artifacts.py
.venv/Scripts/python.exe scripts/evaluate.py run --limit 16
```

- `preflight`: confere dependências e disponibilidade do modelo.
- `selftest`: verifica oito controles sintéticos do avaliador; não mede qualidade do LLM.
- `check_artifacts`: confere fontes, hashes, distribuição dos casos e arquivos necessários.
- `run`: executa seis combinações do laboratório e dez casos. Se faltar infraestrutura, registra não executado sem chamar o modelo.

Limites definidos antes das execuções: até 16 grafos por lote, 90 segundos por processo e nenhuma retentativa automática. No lote de referência houve uma chamada por grafo, totalizando 16 chamadas. Cada nova rodada tem registros próprios; suas respostas podem diferir das já apresentadas no relatório.

## Consultar saídas e métricas

| Caminho | Conteúdo |
|---|---|
| `results/raw/<lote>/` | Entradas, prompts, respostas completas, logs, ambiente e avaliações |
| `results/summary/<lote>/` | CSV/JSON consolidados, métricas e reteste offline |
| `data/manifest.json` | Fontes sintéticas e hashes |
| `tests/cases.csv` | Casos, esperados, requisitos e resultados de referência |
| `tests/schema.json` | Contrato de saída |

```powershell
.venv/Scripts/python.exe scripts/audit_metrics.py
```

Esse comando recalcula métricas do CSV de auditoria e verifica sua associação à confirmação humana. Os resultados técnicos iniciais e a confirmação posterior foram preservados separadamente. Não alterar respostas brutas para ajustar julgamentos.

O reteste realizado em `adapter-retest.json` reaplicou controles às mesmas respostas reais, sem novas inferências. A opção `run --variant improved` está implementada, mas não foi a execução usada nesse reteste: ela faria novas inferências. Não confundir rejeição de saídas pelo adaptador com correção da geração do modelo.

## Notas sobre a preparação local

A criação inicial da `.venv` falhou em `ensurepip`. A instalação foi concluída com o pip do runtime externo, usando `-m pip --python .venv/Scripts/python.exe install -e ./Scrapegraph-ai`. Por isso, o pip não está instalado dentro da `.venv` desta máquina; seu gerenciamento usa pip externo. Isso é histórico do ambiente, não um pré-requisito geral.

`prepare_av2.py` é o bootstrap histórico e não deve ser reexecutado sobre arquivos existentes. `summarize_real_run.py` recusa sobrescrever a auditoria após confirmação humana. O gerador do relatório também protege o LaTeX existente contra sobrescrita. Para editar o relatório, trabalhar diretamente em `relatorio/relatorio_av2.tex`.

Ambientes, modelo, clones e rascunhos antigos de PDF/PNG ficam fora do versionamento. Os caminhos absolutos presentes nas evidências são metadados históricos. O [status](status.md) registra a evolução do trabalho, e o [mapa dos repositórios](repositories.md) identifica as fontes de referência.
