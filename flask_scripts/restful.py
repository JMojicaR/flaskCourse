from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode