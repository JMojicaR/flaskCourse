from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField,
                    DateTimeField, RadioField, SelectField,
                    TextAreaField,)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class Formulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad?')
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
    color = SelectField('Color favorito', choices=[('R', 'Rojo'), ('V', 'Verde'), ('A', 'Azul')])
    comentario = TextAreaField()
    submit = SubmitField('Enviar')

@app.route('/informacion', methods = ['GET', 'POST'])
def informacion():
    return render_template('informacion.html')

@app.route('/datos', methods = ['GET', 'POST'])
def datos():
    formulario = Formulario()
    if formulario.validate_on_submit():
        session['nombre'] = formulario.nombre.data
        session['edad'] = formulario.edad.data
        session['sexo'] = formulario.sexo.data
        session['color'] = formulario.color.data
        session['comentario'] = formulario.comentario.data
        return redirect(url_for('informacion'))
    return render_template('datos.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)  # Comentar esta línea en producción