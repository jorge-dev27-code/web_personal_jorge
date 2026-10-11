from flask import Flask, render_template, request
from models import obtener_proyectos, obtener_perfil, obtener_habilidades

app = Flask(__name__)

@app.context_processor
def inyectar_contexto_global():
    return dict(perfil=obtener_perfil(), habilidades=obtener_habilidades())

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    lista_proyectos = obtener_proyectos()
    return render_template('proyectos.html', proyectos=lista_proyectos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje_exito = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mensaje_exito = f"¡Gracias por escribir, {nombre}! Me pondré en contacto contigo pronto."
    return render_template('contacto.html', exito=mensaje_exito)

if __name__ == '__main__':
    app.run(debug=True)
