from ejemplo7 import app, db, Usuarios

with app.app_context():
    persona = Usuarios.query.get(1)
    persona.color = 'Azul'
    db.session.add(persona)
    db.session.commit()

    personas = Usuarios.query.all()
    print(personas)