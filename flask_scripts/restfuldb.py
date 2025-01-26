from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
directorio = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'restfuldb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

class PersonaBD(db.Model):
    nombre = db.Column(db.String(80), primary_key=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def json(self):
        return {'nombre': self.nombre}
    
class Personas(Resource):
    def get(self, nombre):
        persona = PersonaBD.query.filter_by(nombre=nombre).first()
        if persona:
            return persona.json()
        return {'response': 'Persona not found in db'}, 404

    def post(self, nombre):
        persona = PersonaBD(nombre)
        db.session.add(persona)
        db.session.commit()
        return {'response': 'Persona correctly added to db'}, 200

    def delete(self, nombre):
        persona = PersonaBD.query.filter_by(nombre=nombre).first()
        db.session.delete(persona)
        db.session.commit()
        return {'response': 'Persona correctly deleted from db'}, 200
    
class ListaPersonas(Resource):
    def get(self):
        personas = PersonaBD.query.all()
        return [persona.json() for persona in personas]
    
api.add_resource(Personas, '/persona/<string:nombre>')
api.add_resource(ListaPersonas, '/listar')

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode