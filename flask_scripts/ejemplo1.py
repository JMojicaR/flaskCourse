from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def principal():
    return "<h1>Hola, buenos dias</h1>"

@app.route("/adios")
def adios():
    return "<h1>Hasta luego</h1>"

@app.route("/saludar/<nombre>")
def hola(nombre):
    """
    Saludar a una persona
    ---
    parameters:
      - name: nombre
        in: path
        type: string
        required: true
        description: Nombre de la persona a saludar
    responses:
      200:
        description: Saludo con el nombre y la longitud
    """
    longitud = len(nombre)
    return f"<h1>El nombre {nombre} tiene {longitud} letras</h1>"

@app.route("/longitud/<nombre>")
def longitud(nombre):
    """
    Obtener la longitud de una palabra
    ---
    parameters:
      - name: nombre
        in: path
        type: string
        required: true
        description: Palabra para calcular la longitud
    responses:
      200:
        description: Longitud de la palabra
    """
    valor = len(nombre)
    return f"<h2> La palabra {nombre} tiene {valor} letras</h2>"

@app.route("/suma/<int:numero1>/<int:numero2>")
def suma(numero1, numero2):
    """
    Sumar dos números
    ---
    parameters:
      - name: numero1
        in: path
        type: integer
        required: true
        description: Primer número a sumar
      - name: numero2
        in: path
        type: integer
        required: true
        description: Segundo número a sumar
    responses:
      200:
        description: Resultado de la suma
    """
    resultado = numero1 + numero2
    return f"<h1>La suma de {numero1} y {numero2} es {resultado}</h1>"




if __name__ == '__main__':
    app.run()