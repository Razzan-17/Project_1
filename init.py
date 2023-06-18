from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from conf import URI, SECRET, URI_test

db = SQLAlchemy()
lm = LoginManager()


def create_app():
    app = Flask(__name__)
    app.app_context().push()
    app.config['SECRET_KEY'] = SECRET
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    db.init_app(app)
    lm.init_app(app)
    return app
