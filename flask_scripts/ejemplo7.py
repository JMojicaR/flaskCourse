import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))
print(directorio)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#Creacion del modelo de la base de datos
class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text)
    age = db.Column(db.Integer)
    color = db.Column(db.Text)

    def __init__(self, nombre, age, color):
        self.nombre = nombre
        self.age = age
        self.color = color
    
    def __repr__(self):
        texto = f"Usuario('{self.nombre}', age: '{self.age}', color: '{self.color}')"
        return texto
    
