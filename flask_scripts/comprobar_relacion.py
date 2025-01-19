from ejemplo8 import  app, db, Mascota, Juguete, Propietario

with app.app_context():
    mascota1 = Mascota('Firulais')
    mascota2 = Mascota('Rex')
    db.session.add_all([mascota1, mascota2])
    db.session.commit()

    mascotas = Mascota.query.all()
    print(mascotas)

    propietario1 = Propietario('Juan', mascota1.id)
    propietario2 = Propietario('Maria', mascota2.id)
    db.session.add_all([propietario1, propietario2])
    db.session.commit()

    juguete1 = Juguete('Pelota', mascota1.id)
    juguete2 = Juguete('Hueso', mascota2.id)
    db.session.add_all([juguete1, juguete2])
    db.session.commit()

    mascota = Mascota.query.filter_by(nombre='Firulais').first()
    print(mascota)
    mascota.mostrar_juguetes()
