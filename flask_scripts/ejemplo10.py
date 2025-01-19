from flask import Flask
from flask_bcrypt import Bcrypt

generador = Bcrypt()

password = "clavesecreta1"
password_encrypted = generador.generate_password_hash(password)

print(password_encrypted)

verificar = generador.check_password_hash(password_encrypted, password)
print(verificar)

