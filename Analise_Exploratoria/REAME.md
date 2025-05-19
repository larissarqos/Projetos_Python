<h1 align="center">Análise Exploratória - Avaliação de Vinhos</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e19ce114-9306-4fb4-a11d-bb0a49945ac6" alt="img" width="1100"/>


## 📃 Contexto  
Nesse projeto, faremos uma análise exploratória de um dataset sobre vinhos, com informações de preço, país de origem, tipo de uva utilizado na fabricação, pontos em avaliações, dentre outras características. O foco da análise é, de maneira geral, identificar o tipo de uva com vinhos de melhor avaliação, bem como as melhores garrafas por país e preço. A limpeza, tratamento e análise passo a passo se encontram em detalhes em 'analise_vinho.ipynb', o foco dessa documentação são as respostas obtidas através da análise.

***

<br>

## 🛠️ Ferramentas e Métodos Utilizados
- Microsoft Excel (fonte de dados)
- Linguagem Python (pandas, numpy, matplotlib,)
- Limpeza de dados (tratamento de nulos, duplicados e outliers)

***

<br>

## 🎯 Objetivos 
Nossa análise exploratória visa identificar os seguintes pontos:

- Qual o país com o melhor vinho
- Qual a distribuição dos preços dos vinhos
- Relação Preço x Qualidade do vinho
- Tipos de uva x Qualidade do vinho
- Melhores vinhos por faixa de preço


***

<br>

## 🧱 Estrutura do Projeto  

### 🗄 Banco de dados  
| Coluna | Descrição |
|--------|-----------|
| unnamed | Índice |
| country | País de origem do vinho |
| description | Descrição do vinho |
| designation | Vinhedo dentro da adega de origem das uvas |
| points | Número de pontos que o vinho obteve em sua avaliação |
| price | Preço da garrafa de vinho |
| province | Província (estado) onde o vinho foi feito |
| region_1 | Região onde o vinho foi feito |
| region_2 | Região mais específica |
| taster_name | Nome do revisor |
| taster_twitter_handle | Perfil do twitter do avaliador |
| title | Nome e ano do vinho |
| variety | Tipo de uva utilizada na fabricação do vinho |
| winery | Adega onde o vinho foi feito |

***

<br>

### 🍷 Classificação dos vinhos
| Pontuação | Classificação |
|-----------|---------------|
| 98-100 | Classic |
| 94-97  | Superb |
| 90-93  | Excellent |
| 87-89  | Very good |
| 83-86  | Good |
| 80-82  | Acceptable |

***

<br>

### 📍 Respondendo às perguntas da análise

#### 📌 1. Qual o país com o melhor vinho?
Se considerarmos a média de pontos, teremos num top 5:
- **Inglaterra -** média de 91,55 pontos
- **Índia -** média de 90,22 pontos
- **Áustria -** média de 90,19 pontos
- **Alemanha -** média de 89,84 pontos
- **Canadá -** média de 89,38 pontos

Isso se dá especialmente porque são países com baixa produção de vinho, porém com boa avaliação. Ao fazermos a média, a pontuação desses países vai lá pra cima, levando-os a encabeçarem a lista.  

Por outro lado, filtrando países cujo total de vinhos têm pontuação acima de 93 (ou seja, estão entre Superb e Classic), nosso top 5 muda e temos:
- **EUA -** 5.789 vinhos com pontuação acima de 93
- **França -** 2.161 vinhos com pontuação acima de 93
- **Itália -** 1.541 vinhos com pontuação acima de 93
- **Áustria -** 487 vinhos com pontuação acima de 93
- **Portugal -** 468 vinhos com pontuação acima de 93

--

#### 📌 2. Qual a distribuição dos preços dos vinhos?
A maior parte dos vinhos avaliados estavam entre $20,00 e $50,00 dólares, conforme gráfico:
<div align="center">
  <img src="https://github.com/user-attachments/assets/e37cc734-ea2b-4e83-860c-70407ff38049" width="800px" height="300" alt="Distribuição dos preços dos vinhos" />
</div>

<br>

A relação de preço médio por país, de vinhos mais caros e mais baratos, é dada na tabela abaixo:
| País Vinhos Mais Caros | Valor ($) | País Vinhos Mais Baratos | Valor ($) |
|------------------------|-----------|--------------------------|-----------|
| Suíça      |   | Bugária              |     |
| Inglaterra |   | Armênia              |     |
| Alemanha   |   | Índia                |     |
| França     |   | Bósnia e Herzegovina |     |
| Hungria    |   | Ucrânia              |     |

--

#### 📌 3. Relação Preço x Qualidade do vinho
Há sim relação de preço e qualidade: quanto mais caro o vinho, melhor tende a ser sua qualidade, embora tenha sido possível encontrar vinhos mais baratos com boas avaliações também.

<div align="center">
  <img src="https://github.com/user-attachments/assets/fcc043fe-7894-490f-8a6b-619ce5950527" width="600px" height="300" alt="Relação Preço x Qualidade do vinho" />
</div>

--

#### 📌 4. Tipo de uva x Qualidade do vinho
Analisando o tipo de uva por trás das melhores avaliações, obtemos que os 3 melhores tipo são Syrah, Pinot Noir e Nebiollo.

<div align="center">
  <img src="https://github.com/user-attachments/assets/67746695-11ae-44a5-aded-3e093a9aa764" width="500px" height="550" alt="Tipo de uva x Qualidade do vinho" />
</div>

--

#### 📌 5. Melhores vinhos por faixa de preço
É possível encontrar vinhos Superb (94-97 pontos) de até 15 dólares e vinhos Classic de até 50 dólares. A tabela abaixo possui as garrafas de vinho de maior pontuação, por cada faixa de preço:

Faixa de Preço | Preço | Pontuação | País | Vinho | Tipo de Uva |
|--------------|-------|-----------|------|-------|-------------|
| Até $15          | $14  |  94 | Espanha | Osborne NV Pedro Ximenez 1827 Sweet Sherry        | Sherry                   |
| Entre $15 e $30  | $20  |  96 | EUA     | Rulo 2007 Syrah (Columbia Valley (WA)             | Syrah                    |
| Entre $30 e $50  | $44  |  99 | EUA     | Estate Vineyard Chardonnay (Sonoma...)            | Chardonnay               |
| Entre $50 e $100 | $80  | 100 | EUA     | Charles Smith 2006 Royal City Syrah (Columbia...) | Syrah                    |
| Acima de $100    | $150 | 100 | França  | Château Léoville Barton 2010 Saint-Julien         | Bordeaux-style Red Blend |

