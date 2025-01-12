persona = Usuarios.query.get(1)
    persona.color = 'Azul'
    db.session.add(persona)
    db.session.commit()