import os
import shutil

class Fichero:
    def __init__(self, nombre, directorio):
        self.nombre = nombre
        self.directorio = directorio
        self.ruta_total = os.path.join(directorio, nombre)

    def obtener_tipo(self):
            doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
            img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
            software_types = ('.exe', '.py', '.ipynb')

            extension = "." + self.nombre.rsplit(".", 1)

            if extension in doc_types:
                return "Documentos"
            elif extension in img_types:
                return "Imágenes"
            elif extension in software_types:
                return "Software"
            else:
                return "Otros"

    def es_archivo(self):
        return os.path.isfile(self.ruta_total)

    def mover(self):
        tipo = self.obtener_tipo()
        carpeta_destino = os.path.join(self.directorio, tipo)

        shutil.move(self.ruta_total, os.path.join(carpeta_destino, self.nombre))
        print("El archivo", self.nombre, "se ha movido a la carpeta:", tipo)