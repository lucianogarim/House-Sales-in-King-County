# -*- coding: utf-8 -*-
"""
Curso de Python (Seja um Data Scientist)

@author: LUCIANOGARIM
"""
import pandas as pd

ds=pd.read_csv('datasets/kc_house_data.csv')

# Mostre na tela as cinco primeiras linhas do dataset
print(ds.head())

#Mostre o número de colunas e o número de linhas do dataset
print('Tamanho do Dataset',ds.shape)

#Mostre na tela o nome das colunas
print(ds.columns)

#Mostre na tela o conjunto de dados ordenados pela coluna price em ordem crescente
print(ds[['bedrooms','price']].sort_values('price', ascending=True))