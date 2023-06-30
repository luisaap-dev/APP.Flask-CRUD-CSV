# Aplicación CRUD con Flask

Esta es una aplicación Flask que implementa operaciones CRUD básicas utilizando un archivo CSV como almacenamiento de datos. Permite gestionar una lista de registros con información personal.

## Funcionalidades

La aplicación proporciona las siguientes funcionalidades:

- Mostrar la lista de registros existentes.
- Agregar nuevos registros.
- Editar registros existentes.
- Eliminar registros.
- Ver detalles de un registro específico.

## Configuración y ejecución

Sigue estos pasos para configurar y ejecutar la aplicación:

1. Asegúrate de tener Python instalado en tu sistema.

2. Instala las dependencias requeridas ejecutando el siguiente comando: pip install flask


3. Descarga los archivos de la aplicación y colócalos en un directorio de tu elección.

4. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentran los archivos de la aplicación.

5. Ejecuta la aplicación con el siguiente comando: python main.py


6. Accede a la aplicación en tu navegador web ingresando la siguiente URL: [http://localhost:5000](http://localhost:5000).

## Estructura de la aplicación

La aplicación sigue la siguiente estructura de archivos y directorios:

- `main.py`: Archivo principal que contiene el código de la aplicación Flask y define las rutas y controladores para las operaciones CRUD.

- `models.py`: Archivo que contiene la clase `CSVModel`, responsable de interactuar con el archivo CSV para realizar operaciones de lectura, escritura, actualización y eliminación de datos.

- `templates/`: Directorio que contiene las plantillas HTML para las diferentes vistas de la aplicación.

- `index.html`: Plantilla para mostrar la lista de registros existentes.
- `agregar.html`: Plantilla para agregar un nuevo registro.
- `editar.html`: Plantilla para editar un registro existente.
- `mostrar.html`: Plantilla para mostrar los detalles de un registro.

- `static/`: Directorio opcional que puede contener archivos estáticos, como hojas de estilo CSS o imágenes.

## Notas adicionales

- Asegúrate de tener los permisos adecuados en la carpeta donde se encuentra el archivo CSV para permitir la lectura y escritura de datos.

- Puedes personalizar el diseño y la apariencia de las plantillas HTML según tus necesidades modificando los archivos en el directorio `templates/`.

¡Disfruta usando la aplicación CRUD con Flask!


