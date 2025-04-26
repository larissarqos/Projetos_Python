<h1 align="center">Análise Exploratória - Avaliação de Vinhos</h1>

## Contexto
Nesse projeto, faremos uma análise exploratória de um dataset sobre vinhos, com informações de preço, país de origem, tipo de uva utilizado na fabricação, pontos em avaliações, dentre outras características. O foco da análise é responder às perguntas descritas no tópico Objetivos. A limpeza, tratamento e análise passo a passo se encontram em 'analise_vinho.ipynb', o foco dessa documentação são as respostas obtidas através da análise.

## Objetivos
Nossa análise exploratória visa identificar os seguintes pontos:

* Qual o país com o melhor vinho
* Relação Preço x Qualidade do vinho
* Tipos de uva x Qualidade do vinho
* Melhores vinhos por faixa de preço

## Estrutura do Projeto
### 1. Banco de dados
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

<br>

### 2. Classificação dos vinhos
| Pontuação | Classificação |
|-----------|---------------|
| 98-100 | Classic |
| 94-97  | Superb |
| 90-93  | Excellent |
| 87-89  | Very good |
| 83-86  | Good |
| 80-82  | Acceptable |

<br>

### 3. Respondendo às perguntas da análise

**1. Qual o país com o melhor vinho**  
Se considerarmos a média de pontos, teremos num top 5:
* Inglaterra
* Índia
* Áustria
* Alemanha
* Canadá
Isso se dá especialmente porque são países com baixa produção de vinho, porém com boa avaliação. Ao fazermos a média, a pontuação desses países vai lá pra cima, levando-os a encabeçarem a lista.
Por outro lado, selecionando apenas países cujos vinhos têm pontuação acima de 93 (ou seja, estão entre Superb e Classic), nosso top 5 muda e temos:
* EUA
* França
* Portugal
*  
  
**2. Relação Preço x Qualidade do vinho**  
O produto que conta com mais assinantes é o **Magic Box, 35% do total de assinaturas**. Considerando o impacto dos serviços no faturamento, temos:

| Serviço     | Valor da Assinatura | Total de Assinaturas | Faturamento     |
|:-----------:|:-------------------:|:---------------------:|:---------------:|
| Deluxe Box  | R$35,90             | 168                   | R$6.031,20      |
| Magic Box   | R$9,90              | 266                   | R$2.633,40      |
| Premium X   | R$79,90             | 136                   | R$10.866,40     |
| Safe Watch  | R$29,90             | 232                   | R$6.936,80      |
| **Total**   | --                  | **802**               | **R$26.467,80** |

A maioria dos clientes possui nossos serviços mais baratos. Notamos que, apesar de contar com o maior número de assinaturas, Magic Box é o produto com menor impacto no faturamento.

**3. Tipos de uva x Qualidade do vinho**  
Atualmente, contamos com **802 assinantes**. Considerando o estado em que moram, a maior parte deles é do **Rio Grande do Sul (51%)**, seguido do **Paraná (27%)** e **Santa Catarina (22%)**. De acordo com o gênero e faixa etária, a maior parte dos nosso clientes é do **sexo masculino**. A faixa etária predominante é de **35-44 e 54-70, para ambos os sexos**.

**4. Melhores vinhos por faixa de preço**  
De maneira geral, nossos serviços têm boas avaliações a respeito do produto e atendimento. As principais reclamações são sobre a falta de itens e atraso na entrega.
