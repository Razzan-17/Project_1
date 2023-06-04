from flask import render_template, request, redirect, url_for, abort
from datetime import datetime
from hashlib import sha1

from flask_login import login_user, login_required

from forms import LoginForm, RegisterForm
from __init__py import app, db, lm
from models import Product, User
from UserLogin import UserLogin


def hash_psw(psw: str):
    return sha1(bytes(psw, 'utf-8')).hexdigest()


@lm.user_loader
def load_user(user_email):
    return UserLogin().fromDB(user_email)


@app.route('/')
def shop():
    data = Product.query.limit(9).all()
    return render_template('shop.html', data=data)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        form = request.form
        name = form.get('name')
        email = form.get('email')
        psw1 = form.get('password')
        psw2 = form.get('confirm')
        if psw1 == psw2:
            psw = hash_psw(psw1)
            user = User(name=name, email=email, password=psw, date=datetime.utcnow().strftime('%d.%m.%Y'))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login', values='True'))
        else:
            return abort(301)
    else:
        return render_template('register.html', form=form, errors=form.errors)  # redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    error_text = 'Вы не зарегистрированы'
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter(User.email == email).first()
        if user is None:
            return render_template('login.html', form=form, data=error_text)
        hash_psw1 = hash_psw(password)
        if hash_psw1 != user.password:
            return render_template('login.html', form=form, data='Неверный пароль')
        userlogin = UserLogin()
        userlogin.create(user)
        login_user(userlogin)
        return redirect(url_for('shop'))
    else:
        data = ''
        if request.args.get('values') == 'True':
            data = 'Вы успешно зарегистрировались!'
        return render_template('login.html', form=form, data=data)


@app.route('/card/<uuid>')
def card_view(uuid):
    data_db = Product.query.filter(Product.uuid == uuid).all()
    return render_template('card.html', data=data_db)


if __name__ == '__main__':
    app.run(debug=True)




