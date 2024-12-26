from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/gracias')
def gracias():
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    return render_template('gracias.html', nombre=nombre, apellidos=apellidos)

@app.route('/validacion')
def validacion():
    return render_template('validacion.html')

@app.route('/resultado')
def resultado():
    nombre = request.args.get('nombre')
    if nombre == '':
        mensaje = 'campo vacío'
        return render_template('resultado.html', mensaje=mensaje)
    elif nombre != '':
        letter = nombre[0]
        upper_letter = letter.upper()
        has_lower_case = any(c.islower() for c in nombre)
        has_numbers = nombre.isalpha()
        # Nombre inicia con mayuscula 
        if letter == upper_letter:
            # Nombre solo tiene letras mayusculas
            if has_lower_case == False and has_numbers == False:
                mensaje = 1
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre no tiene minusculas
            elif has_lower_case == False and has_numbers:
                mensaje = 2
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre no tiene numeros
            elif has_lower_case and has_numbers == False:
                mensaje = 3
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre correcto
            elif has_lower_case and has_numbers:
                mensaje = 4
                return render_template('resultado.html', mensaje=mensaje)
        elif letter != upper_letter:
            # Nombre solo con caracteres especiales
            if has_lower_case == False and has_numbers == False:
                mensaje = 5
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre solo con numeros
            elif has_lower_case == False and has_numbers:
                mensaje = 6
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre solo con minusculas
            elif has_lower_case and has_numbers == False:
                mensaje = 6
                return render_template('resultado.html', mensaje=mensaje)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pagina404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)