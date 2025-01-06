from ejemplo7 import app, db, Usuarios

with app.app_context():
    db.create_all()

    persona1 = Usuarios('Juan', 25)
    persona2 = Usuarios('Maria', 30)

    db.session.add_all([persona1, persona2])
    db.session.commit()

    personas = Usuarios.query.all()
    print("Consultar todos los usuarios")
    print(personas)

    filtro1 = Usuarios.query.filter_by(nombre='Juan')
    print("Consulta con filtro por nombre")
    print(filtro1)

    filtro2 = Usuarios.query.get(2)
    print("Consulta con filtro por id")
    print(filtro2)

    #Actualizar un registro
    persona = Usuarios.query.get(1)
    persona.nombre = 'Pedro'
    db.session.add(persona)
    db.session.commit()

    # Verificar la actualización
    personas_actualizadas = Usuarios.query.all()
    print("Usuarios actualizados")
    print(personas_actualizadas)