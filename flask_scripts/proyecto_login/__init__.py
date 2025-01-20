import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

gestor = LoginManager()
app = Flask(__name__)

directorio = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'loginbd.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
gestor.init_app(app)
gestor.login_view = 'login'






