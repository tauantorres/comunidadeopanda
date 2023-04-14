from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '42c94634b076aeb145cdc483f30853ff'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, acesse sua conta para continuar.'
login_manager.login_message_category = 'alert-info'

from comunidadeopanda import routes
