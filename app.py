from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.app_context().push()
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
db = SQLAlchemy(app=app)


@app.route('/')
def home():
    test_dict = [{'name': '1.jpg', 'price': 520},
         {'name': '2.jpg', 'price': 300},
         {'name': '3.jpg', 'price': 780},
         {'name': '4.jpg', 'price': 100},
         {'name': '5.jpg', 'price': 620},
         {'name': '6.jpg', 'price': 780},
         {'name': '7.jpg', 'price': 723},
         {'name': '8.jpg', 'price': 45},
         {'name': '9.jpg', 'price': 400},]
    return render_template('shop.html', data=test_dict)


@app.route('/register')
def register():
    render_template('templates/register.html')


@app.route('/login')
def login():
    render_template('templates/login.html')


@app.route('/shop')
def shop():
    render_template('templates/shop.html', count=[1,1,1])


@app.route('/card/<uuid>')
def card_view(uuid):
    render_template('templates/card.html')


if __name__ == '__main__':
    app.run()




