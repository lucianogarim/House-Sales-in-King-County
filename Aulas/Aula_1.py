# -*- coding: utf-8 -*-
"""
Curso de Python (Seja um Data Scientist)
Exercícios da Aula_1
@author: LUCIANOGARIM
"""
import pandas as pd

ds=pd.read_csv('datasets/kc_house_data.csv')

print(' Quantas casas estão disponíveis para compra?')
print(ds.shape[0])

print('Quantos atributos as casas possuem?')
print(ds.shape[1])
 
print('Quais são os atributos das casas?')
print(ds.columns)

print('Qual a casa mais cara?')
print(ds[['id','price']].loc[ds['price']==max(ds['price'])])

print('Qual a casa com o maior número de quartos?')
print(ds[['id','bedrooms']].loc[ds['bedrooms']==max(ds['bedrooms'])])

print('Qual a soma total de quartos do conjunto de dados?')
print(sum(ds['bedrooms']))

print('Quantas casas possuem 2 banheiros?')
print(ds['bathrooms'].loc[ds['bathrooms']>2].count() ) #Access a group of rows and columns by label(s).

print('Qual o preço médio de todas as casas no dataset?')
print(ds['price'].mean())

print('Qual o preço médio de casas com 2 banheiros?')
print(ds['price'].loc[ds['bedrooms']==2].mean())

print('Qual o preço mínimo entre as casas com 3 quartos?')
print(ds['price'].loc[ds['bedrooms']==3].min())

print('Quantas casas possuem mais de 300 m2?') # converter sqft para sqmeters
print(ds['sqft_living'].loc[ds['sqft_living']/10.764 >300].count())

print('Quantas casas tem mais de 2 andares?')
print(ds['floors'].loc[ds['floors'] >2].count())

print('Quantas casas tem vista para o mar?')
print(ds['waterfront'].loc[ds['waterfront']>0].count())

print('Das casas com vista para o mar, quantas tem 3 quartos?')
print(ds['waterfront'].loc[(ds['waterfront']>0) & (ds['bedrooms']==3)].count())