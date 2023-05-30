from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
import models


app = Flask(__name__)
app.debug = True
app.app_context().push()
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db = SQLAlchemy(app=app)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register')
def register():
    render_template('templates/register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form
        email = form.get('email')
        password = form.get('password')
        print(email, password, sep='\n')
        return '<h1>GGGGGG</h>'
    else:
        login_form = LoginForm()
        return render_template('login.html', form=login_form)


@app.route('/shop')
def shop():
    data = models.Product.query.order_by(models.Product.price).all()
    for i in data:
        print(i)
    return render_template('shop.html', data=data)


@app.route('/card/<uuid>')
def card_view(uuid):
    render_template('templates/card.html')


if __name__ == '__main__':
    app.run()




