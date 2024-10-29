import pandas as pd

class analizador:

    def __init__ (self, dataframe):
        self.dataframe = dataframe

    def maximo(self, columna):
        return self.dataframe[columna].max()
    
    def minimo(self, columna):
        return self.dataframe[columna].min()
    
    def mediana(self, columna):
        return self.dataframe[columna].median()
    
    def media(self, columna):
        return self.dataframe[columna].mean()
    
    def desviacion_tipica(self, columna):
        return self.dataframe[columna].std()
