# Pacote R1

Avaliar individualmente antes de conversar. Não consultar private-mapping.json, automatic.csv ou o pacote do outro avaliador.

Preencher annotations.csv; notas 0/1/2, falha crítica 0/1. Seguir a rubrica anexada. Notas humanas não devem ser preenchidas por IA.


## S01 — CT03

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: missing
```html
<html><body><pre>Produto Aurora: preço não informado</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "missing",
      "trecho": "preço não informado"
    }
  ],
  "motivo": "NA"
}
```


## S02 — CT06

Pergunta: Liste os produtos deste catálogo e o valor vigente de cada um.

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


## S04 — CT04

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: conflict
```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Aurora: R$ 99.00
Valores conflitantes, sem indicação de preço vigente.</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": 10.0,
      "fonte": "conflict",
      "trecho": "R$ 10.00"
    },
    {
      "nome": "Produto Aurora",
      "preco_brl": 99.0,
      "fonte": "conflict",
      "trecho": "R$ 99.00"
    }
  ],
  "motivo": "null"
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


## S06 — CT02

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: prices
```html
<html><body><pre>Produto Canela: R$ 15.50
Produto Dália: R$ 0.00</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Canela",
      "preco_brl": 15.5,
      "fonte": "prices",
      "trecho": "R$ 15.50"
    },
    {
      "nome": "Produto Dália",
      "preco_brl": null,
      "fonte": "prices",
      "trecho": "R$ 0.00"
    }
  ],
  "motivo": "null"
}
```


## S07 — CT06

Pergunta: Liste os produtos deste catálogo e o valor vigente de cada um.

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
      "preco_brl": null,
      "fonte": "correct",
      "trecho": "R$ 10.00"
    },
    {
      "nome": "Produto Cedro",
      "preco_brl": null,
      "fonte": "correct",
      "trecho": "R$ 20.00"
    }
  ],
  "motivo": "null"
}
```


## S08 — CT02

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: prices
```html
<html><body><pre>Produto Canela: R$ 15.50
Produto Dália: R$ 0.00</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Canela",
      "preco_brl": 15.5,
      "fonte": "prices",
      "trecho": "R$ 15.50"
    },
    {
      "nome": "Produto Dália",
      "preco_brl": 0,
      "fonte": "prices",
      "trecho": "R$ 0.00"
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


## S10 — CT03

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: missing
```html
<html><body><pre>Produto Aurora: preço não informado</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "missing",
      "trecho": "preço não informado"
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


## S12 — CT04

Pergunta: Extraia os nomes e os preços atuais de todos os produtos deste catálogo.

Fonte: conflict
```html
<html><body><pre>Produto Aurora: R$ 10.00
Produto Aurora: R$ 99.00
Valores conflitantes, sem indicação de preço vigente.</pre></body></html>

```
Referência (consultar estado da revisão humana no plano do lote):
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
Resposta observada:
```text
{
  "produtos": [
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "conflict",
      "trecho": "R$ 10.00"
    },
    {
      "nome": "Produto Aurora",
      "preco_brl": null,
      "fonte": "conflict",
      "trecho": "R$ 99.00"
    }
  ],
  "motivo": "Impossibilidade de determinar o preço vigente devido a valores conflitantes sem indicação de preço vigente."
}
```
