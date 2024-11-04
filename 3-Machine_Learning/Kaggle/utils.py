import numpy as np
import pandas as pd

def clean_weight(df, column='Weight'):
    df[column] = df[column].str.replace('kg', '').astype(float)
    return df.head()

def clean_ram(df, column='Ram'):
    df[column] = df[column].str.replace('GB', '').astype(float)
    return df.head()

def extract_resolution(df, column='ScreenResolution'):
    df[['ancho', 'alto']] = df[column].str.extract(r'(\d+)x(\d+)').astype(float)
    df['Total Resolution'] = df['ancho'] * df['alto']
    df = df.drop(['ancho', 'alto', column], axis=1, inplace = True)


def diccionario_mediana(df, columna):

    medianas = df.groupby(columna)['Price_euros'].median()

    diccionario_mediana = medianas.to_dict()

    return diccionario_mediana

def mapeo_dicc(df,columna, diccionario_mediana):
    df[columna] = df[columna].map(diccionario_mediana)
