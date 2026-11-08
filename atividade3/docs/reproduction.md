# Reprodução AV3 — comandos atuais

Executar na raiz do repositório, que contém atividade2/ e atividade3/. Usar o ambiente local da AV2: Python 3.12, ScrapeGraphAI 2.3.1 no commit indicado, Ollama 0.40.2 e llama3.2 com o digest do config.json. Instalação nova não foi validada; consultar o guia AV2.

## Comandos executados

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s atividade3/tests -v
.\.venv\Scripts\python.exe atividade3/scripts/experiment.py check
.\.venv\Scripts\python.exe atividade3/scripts/experiment.py provisional
.\.venv\Scripts\python.exe atividade3/scripts/consolidate_ai.py atividade3/results/20261108T151915458937-provisional
```

O modo provisional faz 12 chamadas e registra falta de revisão humana prévia. Não equivale a final acadêmica. Cada novo comando cria novo lote/análise; não usar um lote novo para ocultar o anterior. O protocolo e os arquivos efetivos ficam copiados no snapshot. A e B são preservadas em manifestos separados. A configuração antes/depois deve continuar compatível.

Se Ollama estiver desligado, iniciar uma vez:

```powershell
powershell -ExecutionPolicy Bypass -File atividade2/scripts/start_ollama.ps1
```

Esse iniciador foi ajustado à nova estrutura; o servidor já estava ativo na execução de 08/11.

## Revisão humana e bateria final

Conferir docs/reference-review.md e registrar revisão real em data/reference-review.csv. Alterar nome, data, status e justificativa; hashes não são assinatura humana, apenas vínculo com caso/fonte. Mudanças em fonte/referência exigem nova revisão e hash atualizado. Não retroagir a data da revisão para fazer o lote provisório parecer revisado previamente.

Após revisão, este comando fica disponível:

```powershell
.\.venv\Scripts\python.exe atividade3/scripts/experiment.py final
```

Não foi executado com referências aprovadas nesta etapa. Gerará 12 respostas novas em outro diretório. R1 recebe só a pasta R1 (12 saídas); R2 só R2 (CT01/CT05 A/B, quatro). Não revelar versão e F1 antes das notas quando viável. Registrar exposição prévia. Acesso ao repositório completo limita o cegamento.

Preencher correcao/relevancia/suporte com 0/1/2, falha_critica com 0/1 e nome/data/justificativa/exposicao_previa. Avaliadores distintos e independentes. Diferenças de notas/flag exigem consensus.csv separado com participantes. R1/R2 originais são preservados na consolidação.

```powershell
.\.venv\Scripts\python.exe atividade3/scripts/analyze.py atividade3/results/<lote>-final
```

Comando preparado, ainda sem notas humanas reais. Gera tabela, métricas e comparison.html. Denominadores: seis por versão, 12 auto–humano, quatro R1–R2 antes do consenso. Não preencher campos humanos com notas da IA.

## Materiais

O relatório principal é relatorio/relatorio_av3.tex, acompanhado de f1_por_caso.png. Os slides têm versões PPTX e Beamer, com a mesma ordem de 16 slides e oito participantes. Para compilar fora deste ambiente: pdfLaTeX duas vezes no diretório do relatório e no da apresentação, mantendo o caminho relativo do gráfico dos slides. Esses comandos de compilação externa não foram executados aqui.

build_deliverables.py usa Matplotlib 3.11.2 para o gráfico; foi instalado isoladamente em .build/python-libs, sem alterar o ambiente do modelo. build_slides.mjs usa o runtime do Codex e @oai/artifact-tool 2.8.134. Os geradores não substituem revisão editorial: o gerador do relatório recusa sobrescrever um .tex existente. A compilação integrada foi tentada e bloqueada por acesso negado ao Tectonic.

## Cadeia de reconstrução

caso/versão -> request/response -> ID cego -> notas -> consenso -> decisão. No lote atual, notas IA e justificativas estão em arquivos separados, formulários humanos em branco. Snapshot/hashes, digest, schema e mensagens efetivas permitem conferir as condições. Nem hardware nem todas as dependências foram encapsulados; reprodução não garante igualdade token a token.
