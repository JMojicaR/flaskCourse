from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clavesecreta'

class Formulario(FlaskForm):
    nombre = StringField('Nombre')
    submit = SubmitField('Enviar')

@app.route('/', methods = ['GET', 'POST'])
def principal():
    nombre = ''
    enviado = False
    formulario = Formulario()
    if formulario.validate_on_submit():
        enviado = True
        nombre = formulario.nombre.data
        formulario.nombre.data = ''
    return render_template('formularioflask.html', nombre=nombre, enviado=enviado, formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)  # Comentar esta línea en producción