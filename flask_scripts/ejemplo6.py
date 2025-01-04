from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class Formulario(FlaskForm):
    submit = SubmitField('Enviar')

@app.route('/mensaje', methods = ['GET', 'POST'])
def mensaje():
    formulario = Formulario()
    if formulario.validate_on_submit():
        flash('Mensaje de prueba')
        flash('Otro mensaje de prueba')
        flash('Tercer mensaje de prueba')
        return redirect(url_for('mensaje'))
    return render_template('mensaje.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)  # Comentar esta línea en producción