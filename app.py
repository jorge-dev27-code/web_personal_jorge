from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
# app.py
from flask import Flask, render_template, request
from models import obtener_proyectos  # Importamos el Modelo

app = Flask(__name__)

@app.route('/')
def inicio():
    # El controlador decide mostrar la vista de inicio
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    # El controlador le pide los datos al Modelo
    lista_proyectos = obtener_proyectos()
    # El controlador le pasa los datos a la Vista
    return render_template('proyectos.html', proyectos=lista_proyectos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje_exito = None
    if request.method == 'POST':
        # Aquí el controlador procesaría los datos enviados por el usuario
        nombre = request.form.get('nombre')
        mensaje_exito = f"¡Gracias por escribir, {nombre}! Me pondré en contacto contigo pronto."
        
    return render_template('contacto.html', exito=mensaje_exito)

if __name__ == '__main__':
    app.run(debug=True)
