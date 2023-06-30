import csv
import os

class CSVModel:
    def __init__(self):
        self.ruta_archivo_datos = os.path.join(os.path.dirname(__file__), 'data', 'datos.csv')
        self.codificacion_csv = 'utf-8-sig'

    def _abrir_archivo(self, modo):
        return open(self.ruta_archivo_datos, modo, newline='', encoding=self.codificacion_csv)

    def _obtener_lector_csv(self):
        archivo = self._abrir_archivo('r')
        lector = csv.DictReader(archivo)
        return archivo, lector

    def _obtener_escritor_csv(self, nombres_campos):
        archivo = self._abrir_archivo('w')
        escritor = csv.DictWriter(archivo, fieldnames=nombres_campos)
        escritor.writeheader()
        return archivo, escritor

    def _obtener_todas_las_filas(self):
        archivo, lector = self._obtener_lector_csv()
        filas = list(lector)
        archivo.close()
        return filas

    def _guardar_filas(self, filas):
        archivo, escritor = self._obtener_escritor_csv(filas[0].keys())
        escritor.writerows(filas)
        archivo.close()

    def obtener_todos_los_datos(self):
        try:
            _, lector = self._obtener_lector_csv()
            return list(lector)
        except FileNotFoundError:
            return []

    def obtener_datos(self, id):
        try:
            _, lector = self._obtener_lector_csv()
            for fila in lector:
                if fila['id'] == id:
                    return fila
        except FileNotFoundError:
            pass
        return {}

    def agregar_datos(self, datos):
        filas = self._obtener_todas_las_filas()
        ultimo_id = self.obtener_ultimo_id()
        nuevo_id = ultimo_id + 1
        datos['id'] = str(nuevo_id)
        filas.append(datos)
        self._guardar_filas(filas)

    def actualizar_datos(self, id, datos_actualizados):
        filas = []
        try:
            for fila in self._obtener_todas_las_filas():
                if fila['id'] == id:
                    filas.append(datos_actualizados)
                else:
                    filas.append(fila)
            if not filas:
                filas.append(self._obtener_lector_csv().fieldnames)
            self._guardar_filas(filas)
        except FileNotFoundError:
            pass

    def eliminar_datos(self, id):
        filas = []
        try:
            for fila in self._obtener_todas_las_filas():
                if fila['id'] != id:
                    filas.append(fila)
            self._guardar_filas(filas)
        except FileNotFoundError:
            pass

    def obtener_ultimo_id(self):
        try:
            ultimo_id = 0
            for fila in self._obtener_lector_csv():
                ultimo_id = int(fila['id'])
            return ultimo_id
        except FileNotFoundError:
            return 0
