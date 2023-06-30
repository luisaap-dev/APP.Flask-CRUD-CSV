from flask import Flask, render_template, request, redirect
from models import CSVModel

app = Flask(__name__)
csv_model = CSVModel()

@app.route('/')
def index():
    data = csv_model.obtener_todos_los_datos()
    return render_template('index.html', data=data)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        data = obtener_datos_formulario(request.form)
        csv_model.agregar_datos(data)
        return redirect('/')
    return render_template('agregar.html')

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        data = obtener_datos_formulario(request.form)
        csv_model.actualizar_datos(id, data)
        return redirect('/')
    else:
        data = csv_model.obtener_datos(id)
        return render_template('editar.html', data=data)

@app.route('/eliminar/<id>')
def eliminar(id):
    csv_model.eliminar_datos(id)
    return redirect('/')

@app.route('/mostrar/<id>')
def ver(id):
    data = csv_model.obtener_datos(id)
    return render_template('mostrar.html', data=data)

def obtener_datos_formulario(formulario):
    return {
        'nombre': formulario['nombre'],
        'apellidos': formulario['apellidos'],
        'email': formulario['email'],
        'telefono': formulario['telefono'],
        'sexo': formulario['sexo'],
        'direccion': formulario['direccion'],
        'ciudad': formulario['ciudad'],
        'pais': formulario['pais']
    }

if __name__ == '__main__':
    app.run()
