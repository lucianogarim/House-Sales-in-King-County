# -*- coding: utf-8 -*-
"""
Curso de Python (Seja um Data Scientist)
Exercícios da Aula_2
@author: LUCIANOGARIM
"""
import pandas as pd
ds=pd.read_csv('kc_house_data.csv')
#ds.dtypes #para verificar se o tipo de variável da coluna date está correta


#1. Crie uma coluna chamada: "house_age"
	#-Se o valor da coluna "date" for maior que 2014-01-01 -> 'new_house'
	#-Se o valor da coluna "date" for menor que 2014-01-01 -> 'old_house'
ds['date']= pd.to_datetime(ds['date'])
ds['house_age']="house"
age='2014-01-01'
ds.loc[ds['date']>age,'house_age']='new_house'
ds.loc[ds['date']<age,'house_age']='old_house'


#2. Crie uma nova coluna chamada: "dormitory_type"
	#-Se o valor da coluna "bedrooms" for igual a 1 -> 'studio'
	#-Se o valor da coluna "bedrooms" for igual a 2 -> 'apartament'
	#-Se o valor da coluna "bedrooms" for maior que 2 -> 'house'
ds['dormitory_type']="house"
ds.loc[ds['bedrooms']==1,'dormitory_type']='studio'
ds.loc[ds['bedrooms']==2,'dormitory_type']='apartament'
ds.loc[ds['bedrooms']>2,'dormitory_type']='house'


#3. Crie uma nova coluna chamada: "condition_type"
	#-Se o valor da coluna "condition" for menor ou igual a 2 -> 'bad'
	#-Se o valor da coluna "condition" for igual a 3 ou 4 -> 'regular'
	#-Se o valor da coluna "condition" for igual a 5 -> 'good'
ds['condition_type']="house"
ds.loc[ds['condition']<=2,'condition_type']='bad'
ds.loc[(ds['condition']==3) | (ds['condition']==4) ,'condition_type']='regular'
ds.loc[ds['condition']==5,'condition_type']='good'


#4. Modifique o tipo da coluna "condition" para string
ds['condition']=ds['condition'].astype(str)


#5. Delete as colunas: "sqft_living150" e "sqft_lot15"
exclui=['sqft_living15','sqft_lot15']
ds=ds.drop(exclui,axis=1)

#6. Modifique o tipo da coluna "yr_build" para date.
## Aqui é necessario usar o parametro format='%Y' para indicar que os valores da coluna são em ano.
ds['yr_built']= pd.to_datetime(ds['yr_built'],format='%Y')

#7. Modifique o tipo da coluna "yr_renovated" para date.
## Aqui é necessario usar o parametro errors='coarce' que faz com que os valores não que não consigam
# fazer a conversão se tornem NaT (Not a Time)
ds['yr_renovated']= pd.to_datetime(ds['yr_renovated'],format='%Y',errors='coerce')

#8. Qual a data mais antiga de construção?
ds['yr_built'].min()    

#9. Qual a data mais antiga de reforma?
ds['yr_renovated'].min()

#10. Quantos imóveis tem 2 andares?
(ds['floors']==2).value_counts()

#11. Quantos imóveis estão com a condição "regular"?
(ds['condition_type']=='regular').value_counts()

#12. Quantos imóveis estão com a condição "bad" e "possuem vista para o mar"?
((ds['condition_type']=='bad') & (ds['waterfront']==1)) .value_counts()

#13. Quantos imóveis estão com a condição good e são new_house?
((ds['condition_type']=='good') & (ds['house_age']=='new_house')).value_counts()

#14. Qual o valor do imóvel mais caro do tipo studio?
ds.loc[(ds['dormitory_type']=='studio'),'price'].max()

#15. Quantos imóveis do tipo apartament foram reformados em 2015?
ds.loc[(ds['dormitory_type']=='apartament') & (ds['yr_renovated']=='2015-01-01'),'id'].count()
#((ds['dormitory_type']=='apartament') & (ds['yr_renovated']=='2015-01-01')).value_counts()

#16. Qual o maior numero de quartos que um imovel do house possui?
ds.loc[(ds['dormitory_type']=='house'),'bedrooms'].max()

#17. Quantos imóveis new_house foram reformados em 2014?
ds.loc[(ds['house_age']=='new_house') & (ds['yr_renovated']=='2014-01-01'),'id'].count()

#18. Selecione as colunas "id", "date", "price", "floors", "zipcode" pelos métodos:
	#Nome de colunas
	#Indices
	#Indices x Nome de colunas
	#Booleano
ds['id']
ds.iloc[:,0]
ds.loc[:,'id']
cols=[True, False,False, False,False, False,False, False,False, False,False,
      False,False, False,False, False,False, False,False,False, False,False]
ds.loc[:,cols]

#19. Salve um arquivo .csv com somente as colunas do item 10.
idd=ds['id']
idd.to_csv('new.csv',index=False)

import plotly.express as px

data_map=ds[['id','lat','long','price','condition']]
mapa=px.scatter_mapbox(data_map, lat='lat', lon='long', hover_name='id',
               hover_data=['price'],
               color='condition',
               zoom=9,
               size='price',
               height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600,margin={'r':0,'t':0,'l':0, 'b':0})
mapa.show()

mapa.write_html('mapa_house_rocket.html')














