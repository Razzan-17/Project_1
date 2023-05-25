from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE__URI'] = 'sqlite:///DB.db'

db = SQLAlchemy(app=app)


@app.route('')
def home():
    render_template('templates/home.html')


@app.route('/register')
def register():
    render_template('templates/register.html')


@app.route('/login')
def login():
    render_template('templates/login.html')


@app.route('/shop')
def register():
    render_template('templates/shop.html')


@app.route('/card')
def card_view(uuid):
    render_template('templates/card.html')






