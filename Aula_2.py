# -*- coding: utf-8 -*-
"""
Curso de Python (Seja um Data Scientist)
Exercícios da Aula_1
@author: LUCIANOGARIM
"""
import pandas as pd

ds=pd.read_csv('datasets/kc_house_data.csv')

# ====================================
# Como converter tipo de de variaveis
# ====================================

##inteiro para float
#ds['bedroooms']= ds['bedrooms'].astype(float)
#
##float para inteiro 
#ds['bedroooms']= ds['bedrooms'].astype(int)
#
##inteiro para string
#ds['bedroooms']= ds['bedrooms'].astype(str)
#
##string para inteiro
#ds['bedroooms']= ds['bedrooms'].astype( int)
#
##string para date
#ds['date']= pd.to_datetime(ds['date'])


## ====================================
## Criando variaveis
## ====================================
#
#ds['nome_do_luciano']="luciano"
#ds['comunidade_ds']=50
#ds['data_de_abertura']= pd.to_datetime('20-02-28')
#
## ====================================
## Deletando variaveis
## ====================================
#
#ds=ds.drop('nome_do_luciano',axis=1)
##deletando por listas
#ds=ds.drop(['comunidade_ds','data_de_abertura'],axis=1)
#
#
## ====================================
## Seleção variaveis
## ====================================
#
##direto pelos nomes
#print(ds['price'])
#print(ds[['price','id']]) #dois colchetes para listas
#
##pelos indices DADOS[linhas,colunas]
#print(ds.iloc[0:10,0:3])  #iloc procura pelos indices
#
##pelos indices das linhas e nome das colunas
#print(ds.loc[0:10,'price']) #localize pelo nome das colunas
#
## baseado nos indices booleanos (1,0)
##1=True  0=False
#
#cols=[True, False,True, False,True, False,True, False,True, False,True, False,True, False,True, False,True, False,True, False,False]
#
#print(ds.loc[0:10,cols])


## ====================================
## Respondendo as perguntas do CEO
## ====================================

# Qual a data do imóvel mais antigo do portifólio?
ds['date']= pd.to_datetime(ds['date'])
print(ds.sort_values('date', ascending=True).head())


# Quantos imóveis possuem o número máximo de andares?
print(ds['floors'].unique())
print(ds[ds['floors']==3.5][['floors','id']])
print(ds[ds['floors']==3.5].shape)

#Criar uma classificação para os imóveis, separando-os em baixo e alto padrão, de acrodo com o preço.
#Acima de 540.00,00 (alto padrão)
#Abaxio de 540.000,00 (baixo padrão)


ds['level']="standard"

ds.loc[ds['price']>540000,'level']='high_level'
ds.loc[ds['price']<540000,'level']='low_level'


# Gostaria de um relatorio ordenado por preço e contendo as seguintes informações 
#(id do imóvel, data que o imovel ficou disponível para compra, numero de quartos
#tamanho total do terreno, o preço a classificação do imovel (alto e baixo padrão)

report=ds[['id','date','price','bedrooms','sqft_lot','level']].sort_values('price', ascending=False)
report.to_csv('datasets/report_aula02.csv', index=False)


#Plotly - Biblioteca que armazena funções que desenham mapas
#Scatter MapBox - Função que desenha um mapa

import plotly.express as px

data_map=ds[['id','lat','long','price']]
mapa=px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id',
               hover_data=['price'],
               color_discrete_sequence=['fuchsia'],
               zoom=3,
               height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600,margin={'r':0,'t':0,'l':0, 'b':0})
mapa.show()

mapa.write_html('datasets/mapa_house_rocket.html')
























