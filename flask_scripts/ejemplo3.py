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
        mensaje = 'campo vacio'
        return render_template('resultado.html', mensaje=mensaje)
    elif nombre != '':
        first_character = nombre[0]
        if first_character.isdigit():
            mensaje = 'empieza con número'
            return render_template('resultado.html', mensaje=mensaje)
        else:
            upper_letter = first_character.upper()
            starts_with_upper = first_character == upper_letter
            has_lower_case = any(c.islower() for c in nombre)
            has_numbers = any(c.isdigit() for c in nombre)
            # Nombre inicia con mayuscula 
            if starts_with_upper:
                # Nombre solo tiene letras mayusculas
                if not has_lower_case and not has_numbers:
                    mensaje = "Nombre solo tiene letras mayusculas"
                    return render_template('resultado.html', mensaje=mensaje)
                # Nombre no tiene numeros
                elif has_lower_case and not has_numbers:
                    mensaje = "Nombre no tiene numeros"
                    return render_template('resultado.html', mensaje=mensaje)
                # Nombre no tiene minusculas
                elif not has_lower_case and has_numbers:
                    mensaje = "Nombre no tiene minusculas"
                    return render_template('resultado.html', mensaje=mensaje)
                # Nombre correcto
                elif has_lower_case and has_numbers:
                    mensaje = "Nombre correcto"
                    return render_template('resultado.html', mensaje=mensaje)
            # Nombre solo con caracteres especiales
            if not has_lower_case and not has_numbers:
                mensaje = "Nombre solo con caracteres especiales"
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre solo con letras minusculas
            elif has_lower_case and not has_numbers:
                mensaje = "Nombre solo con letras minusculas"
                return render_template('resultado.html', mensaje=mensaje)
            # Nombre solo con numeros
            elif not has_lower_case and has_numbers:
                mensaje = "Nombre solo con numeros 2"
                return render_template('resultado.html', mensaje=mensaje)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pagina404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)