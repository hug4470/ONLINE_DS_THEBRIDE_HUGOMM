doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')

import shutil
import os

path = r"C:\Users\Alumno Prestamo\Downloads"
for archivo in os.listdir(path):
    if os.path.isfile(os.path.join(path, archivo)):
        if archivo.endswith(doc_types):
            shutil.move(os.path.join(path, archivo), r"C:\Users\Alumno Prestamo\Downloads\Documentos")
            print(archivo, "movido a Documentos")
        
        elif archivo.endswith(img_types):
            shutil.move(os.path.join(path, archivo), r"C:\Users\Alumno Prestamo\Downloads\Imágenes")
            print(archivo, "movido a Imágenes")

        elif archivo.endswith(software_types):
            shutil.move(os.path.join(path, archivo),r"C:\Users\Alumno Prestamo\Downloads\Software")
            print(archivo, "movido a Software")
        
        else:
            shutil.move(os.path.join(path, archivo),r"C:\Users\Alumno Prestamo\Downloads\Otros")
            print(archivo, "movido a Otros")