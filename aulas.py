import pandas as pd

data = pd.read_csv('AB_NYC_2019.csv')

print(data.head(3))

# 1. Qtdade PRpoprietários por região

# seleção de colunas
colunas = ['host_id','neighbourhood_group']
colunas_groupby =  ['neighbourhood_group']

# aplicação de operação matemática
view = data.loc[:, colunas].groupby( colunas_groupby).nunique()

print(view)

# 2. preço médio do aluguel por região

colunas = ['price','neighbourhood_group']
colunas_groupby =  ['neighbourhood_group']

view_price = data.loc[:, colunas].groupby(colunas_groupby).mean()

print(view_price)

# 3. Número de avaliações média por tipo de quarto

colunas = ['number_of_reviews', 'room_type']
colunas_groupby = ['room_type']

review = data.loc[:, colunas].groupby(colunas_groupby).mean()

print(review)

# 4. Desvio Padrão do preço do aluguel por região e tipo de quarto

colunas = ['price', 'neighbourhood_group', 'room_type']
colunas_groupby = ['neighbourhood_group', 'room_type']

dev = data.loc[:, colunas].groupby(colunas_groupby).std()

print(dev)
