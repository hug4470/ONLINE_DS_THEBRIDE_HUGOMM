import os
from clase import Fichero
path = r"C:\Users\Alumno Prestamo\Downloads"

def organizador():
    for archivo in os.listdir(path):
        fichero = Fichero(archivo, path)
        
    return fichero.mover()
print("Movindo archivos...")
# IMPRIMIMOS LISTA DE ARCHIVOS EN LA CARPETA DESCARGAS
result_generator = os.walk(os.getcwd(path))
files_result = [x for x in result_generator]
files_result

organizador()