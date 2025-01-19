from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class FormularioAlta(FlaskForm):
    nombre = StringField('Nombre de la mascota: ')
    submit = SubmitField('Agregar mascota')

class FormularioBaja(FlaskForm):
    id = IntegerField('ID de la mascota: ')
    submit = SubmitField('Eliminar mascota')