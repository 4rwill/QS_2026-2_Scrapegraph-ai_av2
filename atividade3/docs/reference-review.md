# Revisão das referências — leitura pela equipe

Estado: **pendente**. Conferir antes da bateria final. Estas respostas foram propostas a partir das fontes, não extraídas de uma saída do modelo. A equipe precisa revisar a pertinência do caso e a exatidão de nomes, valores, null, fonte e trecho. O motivo pode variar na saída do modelo se mantiver o sentido.

Registrar a revisão efetiva em `data/reference-review.csv`, com nome, data, status `aprovado` e justificativa; não basta atribuir o responsável. Se houver correção, atualizar caso/referência e hash e revisar novamente.

## CT01 — funcional

Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: `data/correct.html`

```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Cedro: R$ 20.00</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": 10.0,
      "fonte": "correct",
      "trecho": "Produto Aurora: R$ 10.00"
    },
    {
      "nome": "Produto Cedro",
      "preco_brl": 20.0,
      "fonte": "correct",
      "trecho": "Produto Cedro: R$ 20.00"
    }
  ],
  "motivo": ""
}
```

## CT02 — funcional

Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: `data/prices.html`

```html
<html><body><pre>Produto Canela: R$ 15.50
Produto Dália: R$ 0.00</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [
    {
      "nome": "Produto Canela",
      "preco_brl": 15.5,
      "fonte": "prices",
      "trecho": "Produto Canela: R$ 15.50"
    },
    {
      "nome": "Produto Dália",
      "preco_brl": 0.0,
      "fonte": "prices",
      "trecho": "Produto Dália: R$ 0.00"
    }
  ],
  "motivo": ""
}
```

## CT03 — funcional

Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: `data/missing.html`

```html
<html><body><pre>Produto Aurora: preço não informado</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "missing",
      "trecho": "Produto Aurora: preço não informado"
    }
  ],
  "motivo": "Preço não informado na fonte."
}
```

## CT04 — funcional

Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: `data/conflict.html`

```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Aurora: R$ 99.00
Valores conflitantes, sem indicação de preço vigente.</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "conflict",
      "trecho": "Produto Aurora: R$ 10.00\nProduto Aurora: R$ 99.00"
    }
  ],
  "motivo": "Preços conflitantes, sem indicação de preço vigente."
}
```

## CT05 — sem evidência suficiente

Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: `data/irrelevant.html`

```html
<html><body><pre>Previsão fictícia: céu claro. Nenhum catálogo disponível.</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [],
  "motivo": "Não há catálogo de produtos na fonte; forneça um catálogo."
}
```

## CT06 — variação de CT01

Liste os produtos deste catálogo e o valor vigente de cada um.

Fonte: `data/correct.html`

```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Cedro: R$ 20.00</pre></body></html>
```

Referência proposta:
```json
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": 10.0,
      "fonte": "correct",
      "trecho": "Produto Aurora: R$ 10.00"
    },
    {
      "nome": "Produto Cedro",
      "preco_brl": 20.0,
      "fonte": "correct",
      "trecho": "Produto Cedro: R$ 20.00"
    }
  ],
  "motivo": ""
}
```
