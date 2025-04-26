<h1 align="center">Análise Exploratória - Avaliação de Vinhos</h1>

## Contexto
Nesse projeto, faremos uma análise exploratória de um dataset sobre vinhos, com informações de preço, país de origem, tipo de uva utilizado na fabricação, pontos em avaliações, dentre outras características. O foco da análise é responder às perguntas descritas no tópico Objetivos. A limpeza, tratamento e análise passo a passo se encontram em 'analise_vinho.ipynb', o foco dessa documentação são as respostas obtidas através da análise.

## Objetivos
Nossa análise exploratória visa identificar os seguintes pontos:

* Qual o país com o melhor vinho
* Relação Preço x Qualidade do vinho
* Tipos de uva X Qualidade do vinho
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


| Pontuação | Classificação |
|-----------|---------------|
| 98-100 | Classic |
| 94-97  | Superb |
| 90-93  | Excellent |
| 87-89  | Very good |
| 83-86  | Good |
| 80-82  | Acceptable |

<br>

### 2. Respondendo às perguntas da análise

**1. Qual o faturamento do mês?**  
O faturamento do mês foi de **R$26.467,80**. Caso se mantenha na faixa dos R$25.000, fecharemos o ano com um faturamento de aproximadamente R$300.000.
  
**2. Que serviço é o mais adquirido?**  
O produto que conta com mais assinantes é o **Magic Box, 35% do total de assinaturas**. Considerando o impacto dos serviços no faturamento, temos:

| Serviço     | Valor da Assinatura | Total de Assinaturas | Faturamento     |
|:-----------:|:-------------------:|:---------------------:|:---------------:|
| Deluxe Box  | R$35,90             | 168                   | R$6.031,20      |
| Magic Box   | R$9,90              | 266                   | R$2.633,40      |
| Premium X   | R$79,90             | 136                   | R$10.866,40     |
| Safe Watch  | R$29,90             | 232                   | R$6.936,80      |
| **Total**   | --                  | **802**               | **R$26.467,80** |

A maioria dos clientes possui nossos serviços mais baratos. Notamos que, apesar de contar com o maior número de assinaturas, Magic Box é o produto com menor impacto no faturamento.

**3. Qual o perfil dos nossos clientes?**  
Atualmente, contamos com **802 assinantes**. Considerando o estado em que moram, a maior parte deles é do **Rio Grande do Sul (51%)**, seguido do **Paraná (27%)** e **Santa Catarina (22%)**. De acordo com o gênero e faixa etária, a maior parte dos nosso clientes é do **sexo masculino**. A faixa etária predominante é de **35-44 e 54-70, para ambos os sexos**.

**4. Qual a avaliação dos nossos serviços?**  
De maneira geral, nossos serviços têm boas avaliações a respeito do produto e atendimento. As principais reclamações são sobre a falta de itens e atraso na entrega.

<br>

### 3. Como melhorar nosso faturamento e atendimento?
De acordo com a análise dos dados, segue sugestões de ações para melhorias:

**Relativas ao faturamento**

* **Oferecer upgrades das assinaturas:** Podemos incentivar nossos clientes a adquirirem nossos serviços de maior preço, através de campanhas focadas no diferencial que esses produtos têm a oferecer.  Um maior número de assinaturas do Premium X, por exemplo, geraria um aumento significativo em nosso faturamento.

* **Aumentar a quantidade de clientes no Paraná e Santa Catarina:** O Rio Grande do Sul detém mais da metade de nossas assinaturas, pensemos em como expandir nossos serviços também nos outros estados. Podemos incluir campanhas de marketing para aumentar as vendas nesses estados, descontos para clientes que indicarem o serviço e mesmo promoções voltadas para leads dessa região.

* **Investir nos perfis que mais contrataram nossos serviços:** A maioria de nossos assinantes possui faixa etária entre 35-44 e 54-70. O impacto de gênero em nosso faturamento não é tão significativo, o que significa que podemos voltar nossas campanhas para ambos os sexos. Começar pedindo feedback desse perfil de clientes sobre nossos produtos (porque adquiriram/recomendariam) será um bom norte para basear nossas campanhas de marketing.

**Relativas ao atendimento**
* **Melhorar a qualidade das nossas entregas:** A maior parte das reclamações de nossos clientes têm relação com a entrega (faltando item, atraso na entrega, embalagem danificada, produto com defeito). Devemos direcionar essas reclamações ao setor responsável pelo embalamento e despacho dos produtos e certificar-se de que está sendo feito corretamente, de que há teste do produto antes do envio e verificação de que todos os itens estão na embalagem. Para além disso, avaliar junto à transportadora quais as causas de atraso na entrega e o que pode ser feito a respeito disso.

* **Analisar a qualidade do suporte ao cliente:** É preciso avaliar a qualidade do nosso suporte, se os canais têm bom atendimento, se é atencioso com nossos clientes. Quanto tempo até a solução das queixas? As soluções oferecidas levam à satisfação dos clientes? Propor desconto nas mensalidades em caso de erros da empresa e agilizar a troca de produtos com defeito pode amenizar as reclamações relacionadas ao atendimento. 


