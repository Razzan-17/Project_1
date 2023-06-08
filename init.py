from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db.init_app(app)
lm.init_app(app)
