import csv
import os

class CSVModel:
    def __init__(self):
        self.ruta_archivo_datos = os.path.join(os.path.dirname(__file__), 'data', 'datos.csv')
        self.codificacion_csv = 'utf-8-sig'

    def obtener_todos_los_datos(self):
        try:
            with open(self.ruta_archivo_datos, 'r', encoding=self.codificacion_csv) as archivo:
                lector = csv.DictReader(archivo)
                return list(lector)
        except FileNotFoundError:
            return []

    def obtener_datos(self, id):
        try:
            with open(self.ruta_archivo_datos, 'r', encoding=self.codificacion_csv) as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    if fila['id'] == id:
                        return fila
        except FileNotFoundError:
            pass
        return {}

    def agregar_datos(self, datos):
        ultimo_id = self.obtener_ultimo_id()
        nuevo_id = ultimo_id + 1
        datos['id'] = str(nuevo_id)

        nombres_campos = ['id'] + list(datos.keys())

        try:
            with open(self.ruta_archivo_datos, 'a', newline='', encoding=self.codificacion_csv) as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=nombres_campos)
                if archivo.tell() == 0:
                    escritor.writeheader()
                escritor.writerow(datos)
        except FileNotFoundError:
            pass

    def actualizar_datos(self, id, datos_actualizados):
        filas = []
        try:
            with open(self.ruta_archivo_datos, 'r', encoding=self.codificacion_csv) as archivo:
                lector = csv.DictReader(archivo)
                nombres_campos = lector.fieldnames
                for fila in lector:
                    if fila['id'] == id:
                        filas.append(datos_actualizados)
                    else:
                        filas.append(fila)
            if not filas:
                filas.append(nombres_campos)
            with open(self.ruta_archivo_datos, 'w', newline='', encoding=self.codificacion_csv) as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=nombres_campos)
                escritor.writeheader()
                escritor.writerows(filas)
        except FileNotFoundError:
            pass

    def eliminar_datos(self, id):
        filas = []
        try:
            with open(self.ruta_archivo_datos, 'r', encoding=self.codificacion_csv) as archivo:
                lector = csv.DictReader(archivo)
                nombres_campos = lector.fieldnames
                for fila in lector:
                    if fila['id'] != id:
                        filas.append(fila)
            with open(self.ruta_archivo_datos, 'w', newline='', encoding=self.codificacion_csv) as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=nombres_campos)
                if filas:
                    escritor.writeheader()
                    escritor.writerows(filas)
        except FileNotFoundError:
            pass

    def obtener_ultimo_id(self):
        try:
            with open(self.ruta_archivo_datos, 'r', encoding=self.codificacion_csv) as archivo:
                lector = csv.DictReader(archivo)
                ultimo_id = 0
                for fila in lector:
                    ultimo_id = int(fila['id'])
                return ultimo_id
        except FileNotFoundError:
            return 0
