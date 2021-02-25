#--------------------------------------
# Libraries
#--------------------------------------
import pandas as pd
from geopy.geocoders import Nominatim
import plotly.express as px
import numpy as np

#--------------------------------------
# Function
# Requisitos de uma função:
# 1. Nome - Em relação a sua responsabilidade
# 2. Input - Parâmetros de entradas
# 3. Output - Dados de Saída
#--------------------------------------
def show_dtypes(data):
    print(data.dtypes,end='\n\n')
    
    return None

def show_dimensions(data):
    print('Number of rows:{}'.format(data.shape[0]),end='\n\n')
    print('Number of columns:{}'.format(data.shape[1]),end='\n\n')
    
def collect_geodata(data,cols):
    

    # initialize API
    geolocator=Nominatim (user_agent='geopiExercises')
    data=data.head(20)
    
    # create empty columns
    data.loc[:,cols[0]]='NA'
    data.loc[:,cols[1]]='NA'

    for i in range(len(data)):
        print('Loop {}/{}'.format(i, len(data)))
        query=str(data.loc[i,'lat']) + ',' + str(data.loc[i,'long'])
        response=geolocator.reverse(query)

        if cols[0] in response.raw['address']:
            data.loc[i, 'house_number']=response.raw['address'][cols[0]]

        if cols[1] in response.raw['address']:
            data.loc[i, 'road']=response.raw['address'][cols[1]]
            
    return data

def data_collect(path):
    # load dataset
    data=pd.read_csv('kc_house_data.csv')

    #1.1 Extraction Analysis
    # data dimensions
    show_dimensions(data)
    # data types
    show_dtypes(data)
    return data

def data_transform(data):
    # convert object to date
    data['date']=pd.to_datetime(data['date'])
    data.dtypes

    # descriptive statistics
    num_attributes = data.select_dtypes(include=['int64','float64'])

    # central tendency - mean, median
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    media = pd.DataFrame( num_attributes.apply(np.mean,axis=0) )
    mediana = pd.DataFrame( num_attributes.apply(np.median,axis=0) )

    # dispersion - std, min, max
    std = pd.DataFrame( num_attributes.apply(np.std,axis=0) )
    max_ = pd.DataFrame( num_attributes.apply(np.max,axis=0) )
    min_ = pd.DataFrame( num_attributes.apply(np.min,axis=0) )

    df1=pd.concat([max_,min_,media,mediana,std],axis=1).reset_index()
    df1.columns = ['attributes', 'max', 'min', 'media', 'mediana', 'std']

    data['dormitory_type']='NA'

    for i in range(len(data)):
        if data.loc[i,'bedrooms']==1:
            data.loc[i,'dormitory_type']= 'studio'
        elif data.loc[i,'bedrooms']==2:
            data.loc[i,'dormitory_type']= 'apartament'
        else:
            data.loc[i,'dormitory_type']= 'house'

    show_dimensions(data)

    data['dormitory_type']='NA'

    for i in range(len(data)):
        if data.loc[i,'bedrooms']==1:
            data.loc[i,'dormitory_type']= 'studio'
        elif data.loc[i,'bedrooms']==2:
            data.loc[i,'dormitory_type']= 'apartament'
        else:
            data.loc[i,'dormitory_type']= 'house'

    show_dimensions(data)       

    data['level']='NA'
    for i in range(len(data)):
        if data.loc[i,'price']<= 321950:
            data.loc[i,'level']=0
        elif (data.loc[i,'price']> 321950) & (data.loc[i,'price']< 450000):
            data.loc[i,'level']=1
        elif (data.loc[i,'price']> 450000) & (data.loc[i,'price']< 645000):
            data.loc[i,'level']=2
        else:
            data.loc[i,'level']=3

    cols=['road','house_number']
    df=data.head(20)
    df2=collect_geodata(df,cols)
    show_dimensions(df2)
    
    return data

def data_load(data):
    # map 
    # usar copy para fazer uma cópia física. Senão é só ponteiro.
    houses=data[['id','lat','long','price','level']].copy()

    fig=px.scatter_mapbox(houses,
                     lat='lat',
                     lon='long',
                     color='level',
                     size='price',
                     color_continuous_scale=px.colors.cyclical.IceFire,
                     size_max=15,
                     zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r':0, 'l':0,'b':0,'t':0})
    fig.show()
    
    return None


if __name__=='__main__':
    # ETL
    
    # Collect
    data_raw=data_collect('kc_house_data.csv')
    
    # Transform
    data_processing=data_transform(data_raw)
    
    # Load
    data_load(data_processing)