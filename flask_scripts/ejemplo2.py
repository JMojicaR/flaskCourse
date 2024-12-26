from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def portada():
    return render_template("portada.html")

@app.route('/json-example', methods=['POST'])
def json_example():
    if request.is_json:
        data = request.get_json()
        return jsonify(data), 200
    else:
        return "Content type is not supported", 400

@app.route('/hola')
def hola():
    valor = 'Antonio'
    diccionario = {'Nombre':'antonio', 'Apellido':'lopez', 'Edad': 25}
    return render_template("hola.html", datos = diccionario)

@app.route('/colores')
def colores():
    colores = ['rojo', 'verde', 'azul']
    return render_template("colores.html", colores = colores)

@app.route('/frase/<texto>')
def frase(texto):
    return render_template("frase.html", tipo = texto)


if __name__ == '__main__':
    app.run()
