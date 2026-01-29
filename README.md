# Health Insurance Cross-Sell

## Descrição
Uma Empresa que atualmente trabalha com seguros de Saúde está avaliando
a possibilidade de começar a também oferecer seguros automotivos para seus
clientes. Entretanto, a empresa não possui recursos suficientes para entrar em
contato com todos os clientes, por isso ela precisa descobrir quais dos clientes atuais
possuem a maior propensão de compra para entrar em contato.

## Objetivo
O objetivo desse projeto será construir um algoritmo de Machine Learning que determine
quais são os clientes com maior propensão de compra entre os consultados. Além disso, 
 de oferecer uma estimativa sobre a porcentagem desses clientes que realmente vão
aceitar a oferta, dependendo da quantidade de clientes que serão contactados. 



# Planejamento da solução
## Produto final
O produto final será composto pelos seguintes items:

1) A criação de um modelo treinado utilizando o algoritmo que apresentar a melhor
performance.

2) Os notebooks nos quais é possível observar todo o procoesso de criação da solução.

3) O desenvolvimento de uma API na qual é possível consultar os clientes com maior
propensão de compra dentre uma lista de clientes pré informada.





## Algoritmos utlizados

### Feature Selection:
Algoritmos: Boruta e ExtraTreesClassifier

### Classificação:
Algoritmos: Logistic Regression, KNN, ExtraTrees, Random Forest e XGBoost

Métricas de performance: Precision_top_K, Recall_top_K, Propensity Score, Cummulative Gain Curve,
Lift Curve

## Ferramentas utilizadas
Python, Scikit-learn e Flask API

# Desenvolvimento


## Estratégia da solução
O projeto foi desenvolvido utilizando a Linguagem Python, utlizando a
biblioteca Pandas para manipulação dos dados e biblioteca Seaborn para
exibição dos gráficos. 

Foram utilizadas as bibliotecas Scikit-learn e XGBoost para treinamento
do algoritmo ML de regressão, além do framework Flask para deploy 
na web.


## O passo a passo
Passo 1: Divisão dos dados em treino e teste, além de efetuar uma estatística
descritiva nos dados a fim de compreensão dos mesmos.

Passo 2: Feature engeenring.

Passo 3: Limpeza de colunas e Linhas no Dataset.

Passo 4: Análise Exploratória dos Dados, com o objetivo de identificar relações entre as features e a target.

Passo 5: Preparação dos dados, efetuando as normalizações, encodings e transformações
de natureza necessárias

Passo 6: Feature selection: determinar quais as features mais representativas para uso dos
modelos de Machine Learning.

Passo 7: Treino dos algoritmos de machine learning, utilizando a técnica de cross-validation.
Efetuar a comparação de performance de aprendizado dos algorimos. 

Passo 8: Pegar o melhor algoritmo do passo anterior e variar os parâmetros, com o objetivo
de encontrar o conjunto de parâmetros que determina a melhor performance do algoritmo.

Passo 9: Analisar as métricas de performance encontradas e o impacto financeiro
resultado por elas.


## Resultados

# Resultados dos Algoritmos

![comparacao_algoritmos](
img/comparacao_algoritmos.png)

O Algoritmo que obteve o melhor resultado em ambas as métricas Precision at K e Recall at K foi o XGBoost, seguido de perto pelo Random Forest.

Além da questão da performance em si, os modelos treinados pelo XGBoost costumam ocupar menos memória e espaço em disco comparado com modelos gerados pelo Random Forest ou ExtraTrees. Desta forma o XGBoost se torna a melhor escolha. 

Após o ajuste de hiperparâmetros a performance final do algoritmo foi a seguinte:

| Model   | Precision at k | Recall at k   |
| ------  | --------       | -------       |
| XGBoost | 0.35 +/- 0.01  | 0.57 +/- 0.01 |      |


# Performance na prática

![performace_resultado](
img/performance_resultado.png)

```
- Para alcançar 29% dos interessados em um novo seguro automotivo, é necessário contactar 10% dos clientes atuais;
- Para alcançar 55% dos interessados em um novo seguro automotivo, é necessário contactar 20% dos clientes atuais;
- Para alcançar 82% dos interessados em um novo seguro automotivo, é necessário contactar 33% dos clientes atuais;
- Para alcançar 98% dos interessados em um novo seguro automotivo, é necessário contactar 50% dos clientes atuais.
```



## Uso da API

Foi desenvolvida uma API de forma como o CFO possa obter de forma personalizada a previsão para um ou mais clientes de
forma segmentada conforme a necessidade. 

Para facilitar o uso da API foi criado o arquivo **previsao.py**, no qual é possível informar a id do cliente inicial e a quantidade de clientes subjacentes a serem classificados. Um exemplo de uso seria:

```
$ python3 previsao.py 381110 5
```

Serão pesquisados os 5 ids a partir do primeiro informado (381110)
O Resultado obtido será semelhante ao abaixo:


```
       id     score
0  381111  0.295314
1  381112  0.179903
2  381113  0.014398
3  381114  0.002474
4  381110  0.001604
```

Dentre os 5 clientes pesquisados, o id 381111 deve ser o primeiro a ser contactado, pois seu score é maior de todos. 
Em seguida o id 381112, e assim por diante.

