import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = '5391628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/saharsh/Desktop/chattingApp/chatApp/chapp.db'
app.config['SQLALCHEMY_BINDS'] = {
    'rooms': 'sqlite:////home/saharsh/Desktop/chattingApp/chatApp/room.db'
}

# SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

socketio = SocketIO(app)

from chatApp import routes, models