# AV2 - ScrapeGraphAI: Contexto Confiável
Diretório de avaliação independente. Estado real em docs/status.md. Missão C aprovada pelo usuário. Clones e AV1 preservados. Vídeo: PENDENTE.

## Reprodução
Diretório: C:/Projetos/QS_2026-2_Scrapegraph-ai_Atividade2. Python 3.12; o executável usado nesta sessão foi C:/Users/chris/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe. Nos comandos abaixo, `python` significa esse executável ou um ambiente Python 3.12 configurado.

Comandos locais verificados: `python scripts/evaluate.py preflight`; `python scripts/evaluate.py selftest`; `python scripts/evaluate.py run --limit 16` (último bloqueia antes de chamar modelo se pré-requisitos faltarem).

Ambiente .venv preparado e import de SmartScraperGraph verificado. A criação inicial falhou em ensurepip; a instalação foi concluída usando o Python do runtime com `-m pip --python .venv/Scripts/python.exe install -e ./Scrapegraph-ai`. Pip não está instalado dentro da .venv; gerenciamento requer pip externo. Versões em results/evidence/dependencies.txt. Ollama portátil 0.40.2 e llama3.2:latest instalados em .tools/ollama; preflight passou em 10/10/2026 às 17:59 -03:00. Reiniciar serviço local: `powershell -File scripts/start_ollama.ps1`. Confirmar digest no preflight. Usar `.venv/Scripts/python.exe` nos comandos de avaliação.

16 execuções de grafo por lote no máximo; 90 s por execução; sem retries. Saídas em results/raw/<lote>; sumário e métricas em results/summary/<lote>. Fontes/prompts/schema congelados e hashes registrados. Tests V01..04 verificam apenas adaptador. Melhoria local: `--variant improved` aplica rejeição determinística sem reescrever a saída bruta; executar baseline primeiro e comparar com mesmo digest. Não confundir rejeição com correção do modelo.

Materiais: docs/mission.md, system-card.md, methodology.md, threats.csv, findings.csv, improvement-plan.csv, report.md, presentation.md, video-script.md, manual-checklist.md; prompts; tests/cases.csv/schema.json; data/manifest.json. PDF/slides finais dependem dos resultados e revisão. Submissão acadêmica pendente.

## Resultados reais disponíveis
Lote 20261010T175910-baseline: 16 respostas reais e 16 chamadas, seis LAB e dez CT. Análise para os materiais: docs/results-analysis.md. Métricas e evidências em results/summary e results/raw. Usuário fará documento, slides e vídeo; PDFs anteriores são rascunhos desatualizados. Auditoria técnica de cinco afirmações preparada, revisão humana pendente. Confirmação presencial com professor declarada pelo usuário em decisions.md.

## Reprodução em outra máquina

Repositório AV2: https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2. Python 3.12 e Git necessários. Os clones internos não são parte do commit. Preparação abaixo ainda não executada em uma máquina limpa:

```powershell
git clone https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2.git
cd QS_2026-2_Scrapegraph-ai_av2
git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git Scrapegraph-ai
git -C Scrapegraph-ai checkout --detach 194055e203afce41ed4e70365dbc416bad756115
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements-evaluation.txt
```

Instalar Ollama pela distribuição oficial, iniciar serviço local e executar `ollama pull llama3.2:latest`. Se já houver serviço Ollama, não executar start_ollama.ps1. Esse script serve apenas para a instalação portátil em .tools/ollama. Conferir o digest informado no preflight antes de comparar resultados.

```powershell
.venv/Scripts/python.exe scripts/evaluate.py preflight
.venv/Scripts/python.exe scripts/evaluate.py selftest
.venv/Scripts/python.exe scripts/check_artifacts.py
.venv/Scripts/python.exe scripts/evaluate.py run --limit 16
```

Os comandos de avaliação foram executados neste computador. requirements-evaluation.txt contém as versões observadas, com caminho editável relativo. A instalação completa por esse arquivo em ambiente limpo ainda está pendente. Para apenas inspecionar as evidências, não é necessário baixar o modelo. prepare_av2.py é o bootstrap histórico desta máquina e não deve ser reexecutado sobre arquivos existentes. summarize_real_run.py regenera a auditoria técnica do lote fixo; não rodar sobre uma auditoria já revisada por humanos.

Arquivos locais excluídos do Git: ambientes, Ollama/modelos, clones, PDFs/PNGs de rascunhos e transcrições integrais de PDFs acadêmicos. Os hashes/origens dos PDFs e registros brutos de avaliação permanecem disponíveis. Os caminhos absolutos nas evidências são metadados históricos.
