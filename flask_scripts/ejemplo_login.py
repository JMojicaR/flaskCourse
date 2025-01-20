from proyecto_login import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from proyecto_login.modelos import Usuario
from proyecto_login.formulario import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/bienvenida')
@login_required
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/salir')
@login_required
def salir():
    logout_user()
    flash('Has salido de la sesión.')
    return redirect(url_for('principal'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario is not None and usuario.verificar_password(form.password.data):
            login_user(usuario)
            flash('Has iniciado sesión.')
            proxima_pagina = request.args.get('next')
            if proxima_pagina is None or not proxima_pagina.startswith('/'):
                proxima_pagina = url_for('bienvenida')
            return redirect(proxima_pagina)
    return render_template('entrar.html', form=form)
    
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistrationForm()
    if form.validate_on_submit():
        usuario = Usuario(nombre=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Gracias por registrarte.')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)