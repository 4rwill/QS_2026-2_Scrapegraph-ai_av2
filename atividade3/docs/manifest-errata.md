# Caminhos dos manifestos após reorganização

Os manifestos base de A/B foram atualizados após a publicação dos resultados. Nas cópias congeladas do lote, o campo descritivo code ainda menciona o caminho antigo ../../scripts/evaluate.py. O worker efetivamente executado é snapshot/atividade2/scripts/evaluate.py, preservado e vinculado em snapshot-hashes.json; o executor congelado em snapshot/atividade3/scripts/experiment.py mostra esse caminho real. O schema correspondente está em snapshot/atividade2/tests/schema.json.

Essa correção é documental, não alteração de saída, referência, prompt ou métrica. Os manifestos e snapshots originais do lote permanecem sem reescrita. Caminhos antigos nas evidências históricas da AV2 devem ser interpretados a partir de atividade2/, conforme a reorganização.
