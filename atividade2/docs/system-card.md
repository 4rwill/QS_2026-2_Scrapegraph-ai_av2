# Ficha do sistema
Projeto: ScrapeGraphAI, https://github.com/ScrapeGraphAI/Scrapegraph-ai, MIT (LICENSE do clone). Commit e versão em repositories.md. Finalidade: extração por linguagem natural; usuários: desenvolvedores e analistas.

Fluxo observado no código: usuário → prompt/schema → FetchNode (HTML sintético) → GenerateAnswerNode → Ollama → JSON → validador/evidências. html_mode=true desativa ParseNode neste recorte; não há busca RAG nem seleção de fontes externas. reasoning e reattempt ficam desativados.

Provedor proposto: Ollama; modelo solicitado llama3.2:latest, temperatura 0, contexto 8192. Versão e digest reais devem vir de /api/version e /api/tags em cada lote; latest não é pin imutável. Python 3.12.14; ScrapeGraphAI/langchain foram instalados na .venv e importados com sucesso. Versões em results/evidence/dependencies.txt. Ollama localhost:11434 recusou conexão em 10/10/2026; usuário confirmou que não está instalado. Não pressupor ambiente da AV1 disponível aqui.

Dados sintéticos: data/fixtures; históricos públicos da AV1 apenas como referência. Dados internos, pessoais reais e segredos não autorizados. Nenhuma ação externa no recorte. Prompts internos do grafo também serão capturados pelo callback; ausência dessa captura torna rastreabilidade incompleta.

Atualização após instalação: Ollama portátil 0.40.2 e llama3.2:latest disponíveis, digest a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72. Temperatura 0, num_ctx real 8192; GPU GTX 1650. Lote 20261010T175910-baseline executou 16 grafos/16 chamadas, com mensagens internas e respostas brutas capturadas.
