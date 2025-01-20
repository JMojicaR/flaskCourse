from proyecto_login import db, gestor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@gestor.user_loader
def cargar_usuario(Usuario_id):
    return Usuario.query.get(int(Usuario_id))

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text)
    email = db.Column(db.String(64), unique=True, index=True)
    nombre = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        texto = f"Usuario('{self.nombre}', email: '{self.email}')"
        return texto