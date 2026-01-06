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
dos algoritmos de machine Learning, além do framework Flask para deploy 
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

Passo 9: Determinar as métricas encontradas


# Resultados

# Resultados dos Algoritmos

![comparacao_algoritmos](
img/comparacao_algoritmos.png)

O Algoritmo que obteve o melhor resultado em ambas as métricas Precision at K e Recall at K foi o XGBoost, seguido de perto pelo Random Forest.

Além da questão da performance em si, os modelos treinados pelo XGBoost costumam ocupar menos memória e espaço em disco comparado com modelos
gerados pelo Random Forest ou ExtraTrees. Desta forma o XGBoost se torna a melhor escolha. 

Após o fine tuning dos hyperparamentros do XGBoostRegressor, a performance econtrada se mostrou levemente melhor que a performance inicial do RandomForestRegressor.

![classificacao_treinamento](
img/finetuning_algoritmo.png)






# Conclusão

Nesse ensaio de Machine Learning, consegui adquirir experiência e
entender melhor sobre os limites dos algoritmos entre os estados de
underffiting e overfitting.

Algoritmos baseados em árvores são sensíveis quanto a profundidade do
crescimento e do número de árvores na floresta, fazendo com que a
escolha correta dos valores desses parâmetros impeçam os algoritmos de
entrar no estado de overfitting.

Alguns testes de algoritmos, como por exemplo a Regressão Polinomial, demoram
muito tempo para serem executados na busca dos melhores parâmetros. Isso demonstra
a necessidade de escolher melhores estratégias na escolha dos valores dos parâmetros
a serem testados. Uma ferramenta que pode ser usada neste caso é RandomizedSearchCV,
onde são são sorteados aleatorimente uma quantidade de valores definida pelo usuário,
dentro de todos os valores escolhidos.

Foi observado que os algoritmos de regressão e clusterização não apresentaram
boas métricas de performance, o que demonstra que somente variar os valores dos
parâmetros pode não ser suficiente. Isso mostra uma necessidade de uma seleção
de atributos e uma preparação melhor das variáveis independentes do conjunto de
dados. Em outras palavras, existe um limite de ganho de performance em tunar
os valores de parâmetros.

Esse ensaio de Machine Learning foi muito importante para aprofundar o
entendimento sobre o funcionamento de diversos algoritmos de
classificação, regressão e clusterização e quais os principais parâmetros
de controle entre os estados de underfitting e overfitting.


# Próximos passos
Como próximos passos desse ensaio, pretendo ensaiar novos algoritmos
de Machine Learning e usar diferentes conjuntos de dados para aumentar
o conhecimento sobre os algoritmos e quais cenários são mais favoráveis
para o aumento da performance dos mesmos.



