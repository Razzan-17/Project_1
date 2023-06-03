from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db.init_app(app)
db.create_all()
