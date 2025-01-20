from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

personas = []

class Personas(Resource):
    def get(self, nombre):
        for persona in personas:
            if persona == nombre:
                return {'nombre': persona}, 200
        return {'Persona no encontrada': nombre}, 404

    def post(self, nombre):
        persona = nombre
        personas.append(persona)
        return {'nombre': persona}, 200

    def delete(self, nombre):
        for indice, persona in enumerate(personas):
            if persona == nombre:
                personas.pop(indice)
                return {'nota': 'borrado exitosamente'}, 200
        return {'nombre': None}, 404
    
class ListaPersonas(Resource):
    def get(self):
        return {'personas': personas}, 200
    
api.add_resource(Personas, '/persona/<string:nombre>')
api.add_resource(ListaPersonas, '/listar')

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode