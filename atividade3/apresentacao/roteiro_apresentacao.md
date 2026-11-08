# Roteiro AV3 — oito participantes, uma sequência

Base: slides_av3.pptx, 16 slides. Dois slides por pessoa, sem retorno de participantes. Meta de 10–12 minutos, incluindo transições; duração depende de ensaio. Os blocos abaixo têm cerca de 1min10–1min30 cada. Reservar 3–5 minutos para perguntas após a apresentação.

**Estado dos materiais:** 12 respostas reais consolidadas; pareceres por IA identificados; revisão humana e decisão experimental final pendentes. Conferir e atualizar slides, relatório e falas se essas etapas forem concluídas antes da apresentação. Não apresentar pareceres da IA como contribuições humanas realizadas.

## 1. Christian Will Silva Santos Nunes — slides 1–2

**Tela:** slide 1 durante a abertura; passar ao slide 2 quando explicar o recorte. Apontar o problema, a extração de catálogo e a comparação A/B. Não abrir terminal nesta parte.

**Fala:**

“Olá, eu sou Christian. Nosso trabalho continua o estudo do SmartScraperGraph, que usa inteligência artificial para extrair informações. Na atividade anterior, vimos que uma resposta pode estar organizada e, mesmo assim, trazer informação incorreta ou um trecho que não permite conferir o resultado.

Nesta atividade, investigamos uma pergunta mais específica: mudar o prompt melhora a resposta? E uma métrica automática consegue representar essa qualidade?

Para isso, mantivemos um fluxo simples: o sistema recebe um catálogo fictício em HTML e precisa extrair nomes e preços, indicando a fonte e o trecho de apoio. Comparamos duas versões do prompt nos mesmos seis casos, usando o mesmo modelo e as mesmas configurações.

Essa escolha permite observar o efeito da mudança de instrução sem reconstruir a aplicação. Também preservamos as entradas e as respostas para conferir o que aconteceu. Agora vamos apresentar o plano que orientou essa comparação.”

## 2. Arthur Soares Santana — slides 3–4

**Tela:** mostrar as duas perguntas GQM no slide 3; no slide 4, destacar CT02, CT05 e a relação CT06–CT01.

**Fala:**

“O planejamento usou GQM: primeiro definimos o objetivo, depois as perguntas e as medidas. Queremos saber se B atende melhor à tarefa e se o sinal automático representa adequação. Para responder, o plano combina F1 lexical, aprovação humana e concordância entre essas decisões.

Fixamos o limiar automático em zero vírgula cinco antes da bateria. Também definimos que uma melhora precisa aparecer no julgamento humano, sem falha crítica ou regressão.

Os casos cobrem um catálogo comum, um produto com preço zero e outro decimal, preço ausente, preços conflitantes e uma fonte sem catálogo. O último caso reformula a pergunta do primeiro, preservando a intenção. Por isso, ele é relacionado ao primeiro, e não uma observação independente.

As referências foram propostas diretamente das fontes sintéticas. A revisão humana prévia ainda está pendente e foi registrada como limitação do lote. Não usamos outra resposta do modelo como única verdade de referência.”

## 3. Eduardo Curcino Monteiro Filho — slides 5–6

**Tela:** slide 5 para as regras existentes; slide 6 para as instruções adicionais. A diferença completa pode ser consultada nas pastas versions/A e versions/B.

**Fala:**

“A versão A reaproveita o prompt estruturado da atividade anterior. Ele pede a extração dos produtos e preços atuais, restringe os fatos ao HTML e proíbe inventar valores ou fontes. Também orienta usar null quando o preço estiver ausente ou em conflito e devolver uma lista vazia quando não houver produtos.

A versão B mantém esse texto e acrescenta instruções mais explícitas. Ela pede que o trecho copie a linha que liga nome e preço, que o produto seja preservado quando faltar valor e que um conflito gere um único registro com null e explicação.

A hipótese era que esse detalhamento melhoraria o apoio e a abstenção. Alteramos somente o prompt como fator principal: modelo, fontes, casos, schema e parâmetros permaneceram iguais.

Como foram adicionadas várias orientações no mesmo prompt, o experimento não consegue separar o efeito de cada frase. E B foi tratada como candidata, sem assumir antecipadamente que seria melhor.”

## 4. Iuri Maurício Maia Pereira — slides 7–8

**Tela:** apontar as configurações no slide 7; no slide 8, explicar a cadeia de evidências. Se houver demonstração adicional, abrir um manifesto salvo; isso é navegação por registros, não execução ao vivo.

**Fala:**

“A execução manteve o SmartScraperGraph na versão dois ponto três ponto um e o mesmo commit usado na AV2. O modelo foi llama três ponto dois, executado localmente pelo Ollama, com temperatura zero e contexto de oito mil cento e noventa e dois tokens.

Foram registradas doze respostas: seis casos em duas versões, uma chamada por combinação. A ordem alternou as versões entre os casos. Havia limite de tempo por processo e nenhuma retentativa automática. Os dois pilotos da preparação ficaram separados e não entram nesse total.

Cada combinação preserva o pedido, o contexto, a resposta, as mensagens do modelo, a configuração e o log. Os manifestos relacionam esses arquivos ao prompt, ao modelo e às fontes. Um snapshot registra o código que realmente foi usado.

Isso permite reconstruir as condições do experimento. Mesmo com temperatura zero, não afirmamos que uma nova execução produzirá exatamente os mesmos tokens.”

## 5. Artur José Soares Santos — slides 9–10

**Tela:** explicar as três dimensões no slide 9 e o estado real das avaliações no slide 10. Não dizer que preencheu R2 enquanto isso não tiver ocorrido.

**Fala:**

“A rubrica separa três dimensões. Correção verifica se os fatos correspondem à fonte. Relevância verifica se a tarefa foi atendida. Suporte verifica se a resposta permite sustentar as afirmações ou justificar uma abstenção. Cada dimensão recebe zero, um ou dois.

A aprovação exige nota dois nas três dimensões e nenhuma falha crítica. Entre as falhas críticas previamente definidas estão inventar produtos e atribuir preço vigente quando a fonte não permite essa conclusão.

O plano humano prevê uma pessoa avaliando as doze saídas e uma segunda revisando apenas os casos um e cinco, nas duas versões. As avaliações devem ocorrer de forma independente, e diferenças precisam de consenso registrado sem apagar as notas originais.

Nesta versão dos materiais, essas avaliações humanas estão pendentes. Os pareceres disponíveis foram produzidos por Codex e estão identificados como IA. Portanto, eles apoiam a análise, mas não completam a exigência de avaliação humana da atividade.”

## 6. Pedro César Figueiredo Carneiro — slides 11–12

**Tela:** slide 11, comparar linhas CT02 e CT06; slide 12, apontar médias e o caso CT05 abaixo do limiar. Explicar a origem das notas C/R/S.

**Fala:**

“O F1 lexical mede a sobreposição de tokens entre a resposta e a referência. Usamos normalização fixa e contamos repetições das palavras. A medida inclui todos os campos do JSON, de modo que chaves, nomes e trechos semelhantes podem aumentar o resultado sem comprovar que o preço está correto.

Na bateria, a média foi aproximadamente zero vírgula sete quatro oito em A e zero vírgula sete zero um em B. Com o limiar de zero vírgula cinco, cinco das seis respostas foram aprovadas automaticamente em cada versão.

Já a rubrica aplicada pela IA não aprovou integralmente nenhuma das doze respostas, principalmente pela insuficiência dos trechos de apoio. Essa é uma comparação automático–IA, e não a concordância com pessoas exigida no plano.

Os denominadores precisam continuar explícitos: seis por versão, doze na concordância automático–humano e apenas quatro na comparação entre os dois avaliadores humanos. As duas últimas medidas ainda aguardam as notas reais.”

## 7. Eduardo Ferreira Bomfim Filho — slides 13–14

**Tela:** no slide 13, comparar preço zero da fonte com null da resposta. No slide 14, apresentar a recomendação técnica e a pendência da decisão humana.

**Fala:**

“Um resultado mostra claramente o limite da similaridade lexical. No caso dois, a fonte informa que o Produto Dália custa zero reais. A versão B devolveu null para esse preço, embora o próprio trecho citado contivesse o valor zero.

Mesmo assim, o F1 foi zero vírgula oito cinco sete, acima do limiar. Grande parte dos nomes, campos e palavras continuou semelhante à referência, mantendo o score alto apesar do erro factual.

Também houve perda na paráfrase do caso seis: B transformou em null os dois preços conhecidos, com F1 de zero vírgula oito. As diferenças entre sinal automático e parecer da IA foram explicadas pelas evidências; o limiar não foi alterado para fazer os resultados coincidirem.

A recomendação técnica é revisar B antes de avançar, pois o detalhamento não corrigiu os trechos e houve perdas factuais. A decisão experimental final permanece pendente de julgamento humano. Manter A como baseline também não significa autorizar uso em produção.”

## 8. Rian Purificação de Oliveira — slides 15–16

**Tela:** slide 15 para os limites e acompanhamento; slide 16 para organização e próximos passos. Encerrar sem devolver a fala a alguém que já participou.

**Fala:**

“As conclusões precisam respeitar os limites do estudo. São seis casos sintéticos, com uma resposta por condição, e o caso seis está relacionado ao primeiro. Não medimos estabilidade em várias repetições nem comportamento em produção. Os pareceres por IA também não permitem calcular concordância entre pessoas.

Como acompanhamento, propomos observar erros factuais, abstenções indevidas e trechos sem apoio suficiente em novos casos, com revisão humana. Se uma mudança introduzir regressão, podemos voltar ao prompt A preservado, sem apagar a versão B ou suas evidências.

O repositório está organizado em atividade dois e atividade três. Os materiais incluem prompts, fontes, manifestos, saídas, tabelas, relatório e a pasta do vídeo informada pela equipe.

Para concluir a atividade, faltam a revisão humana, a decisão final e a conferência dos materiais e contribuições. O uso de Codex como apoio está declarado. O resultado principal desta etapa é mostrar que semelhança lexical alta, sozinha, não garante qualidade factual. Obrigado.”

## Preparação do ensaio

- Cada participante apresenta somente seus dois slides e passa para o próximo bloco.
- Cronometrar o conjunto, visando 10–12 minutos; reduzir pausas ou texto, sem remover limitações que alterem a conclusão.
- Se a revisão humana for concluída, atualizar os slides 3, 9–16 e os blocos correspondentes com notas reais e os denominadores corretos.
- Conferir a pronúncia: F1 (“éfe um”), null (“nulo”), GQM (“gê quê eme”).
- Perguntas prováveis: por que zero difere de null? Por que F1 ficou alto com erro? Por que R1–R2 usa quatro? O que impediria promover B? Como reconstruir uma saída?
