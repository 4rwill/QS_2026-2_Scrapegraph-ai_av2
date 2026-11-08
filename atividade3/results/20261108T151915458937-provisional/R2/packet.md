# Pacote R2

Avaliar individualmente antes de conversar. Não consultar private-mapping.json, automatic.csv ou o pacote do outro avaliador.

Preencher annotations.csv; notas 0/1/2, falha crítica 0/1. Seguir a rubrica anexada. Notas humanas não devem ser preenchidas por IA.


## S03 — CT01

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: correct
```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Cedro: R$ 20.00</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": 10.0,
      "fonte": "correct",
      "trecho": "R$ 10.00"
    },
    {
      "nome": "Produto Cedro",
      "preco_brl": 20.0,
      "fonte": "correct",
      "trecho": "R$ 20.00"
    }
  ],
  "motivo": "NA"
}
```


## S05 — CT01

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: correct
```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Cedro: R$ 20.00</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": 10.0,
      "fonte": "correct",
      "trecho": "R$ 10.00"
    },
    {
      "nome": "Produto Cedro",
      "preco_brl": 20.0,
      "fonte": "correct",
      "trecho": "R$ 20.00"
    }
  ],
  "motivo": "null"
}
```


## S09 — CT05

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: irrelevant
```html
<html><body><pre>Previsão fictícia: céu claro. Nenhum catálogo disponível.</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
```json
{
  "produtos": [],
  "motivo": "Não há catálogo de produtos na fonte; forneça um catálogo."
}
```
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto 1",
      "preco_brl": null,
      "fonte": "irrelevant",
      "trecho": "Previsão fictícia: céu claro. Nenhum catálogo disponível."
    },
    {
      "nome": "Produto 2",
      "preco_brl": null,
      "fonte": "irrelevant",
      "trecho": "Previsão fictícia: céu claro. Nenhum catálogo disponível."
    }
  ],
  "motivo": "Sem catálogo no HTML"
}
```


## S11 — CT05

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: irrelevant
```html
<html><body><pre>Previsão fictícia: céu claro. Nenhum catálogo disponível.</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
```json
{
  "produtos": [],
  "motivo": "Não há catálogo de produtos na fonte; forneça um catálogo."
}
```
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "NA",
      "preco_brl": null,
      "fonte": "irrelevant",
      "trecho": "Previsão fictícia: céu claro. Nenhum catálogo disponível."
    },
    {
      "nome": "NA",
      "preco_brl": null,
      "fonte": "irrelevant",
      "trecho": "Previsão fictícia: céu claro. Nenhum catálogo disponível."
    }
  ],
  "motivo": "NA"
}
```
