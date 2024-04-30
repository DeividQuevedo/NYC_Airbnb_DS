import pandas as pd
import plotly.express as px
import folium as fl
import webbrowser

data = pd.read_csv('AB_NYC_2019.csv')

# 1. Qual o valor do aluguel (diária) mais caro de cada região da base de dados da cidade de NY?

colunas = ['price', 'neighbourhood_group']
colunas_groupby = ['neighbourhood_group']

data_plot = data.loc[:, colunas].groupby(colunas_groupby).max().reset_index()

graph_max = px.bar(data_plot, x='neighbourhood_group', y='price')
graph_max.show()

# 2. Conseguimos saber onde estão localizados os imóveis com o valor do aluguel mais caro, na cidade de NY?

colunas = ['price', 'neighbourhood_group', 'latitude', 'longitude']
colunas_groupby = ['neighbourhood_group']

data_plot2 = data.loc[:, colunas].groupby(colunas_groupby).max().reset_index()

f = fl.Figure(width=1024, height=768)

map = fl.Map(
    location=[data_plot2['latitude'].mean(), data_plot2['longitude'].mean()],
    zoom_start=14,
    control_scale=True
)

for index, location_info in data_plot2.iterrows():
    fl.Marker([location_info['latitude'],
               location_info['longitude']],
               popup=location_info['neighbourhood_group'] ).add_to(map)

map.save('mapa.html')
webbrowser.open('mapa.html')
