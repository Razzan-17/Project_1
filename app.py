from flask import render_template, request, redirect, url_for, abort
from flask_login import login_user, login_required, logout_user, current_user
from UserLogin import UserLogin

from init import create_app, lm
from app_func import hash_password
from forms import LoginForm, RegisterForm
from models import Buyer
from app_func import QueryDataBase as qdb

app = create_app()


@lm.user_loader
def load_user(user_email: str):
    return UserLogin().fromDB(user_email)


@app.route('/')
def shop():
    return render_template('shop.html',
                           data=qdb.query_all())


@app.route('/profile')
@login_required
def profile():
    email = current_user.get_prof().email
    data, summ = qdb.query_profile(email)
    return render_template('profile.html', basket=data, summ=summ)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        form = request.form
        psw = form.get('password')
        if psw == form.get('confirm'):
            qdb.create_user(psw, form)
            return redirect(url_for('login', values='True'))
    else:
        return render_template('register.html', form=form, errors=form.errors)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error_text = 'Вы не зарегистрированы'
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form.get('email')
        password = request.form.get('password')
        user = Buyer.query.filter(Buyer.email == email).first()
        if user is None:
            return render_template('login.html', form=form, data=error_text)
        if user.password != hash_password(password):
            return render_template('login.html', form=form, data='Неверный пароль')
        u_login = UserLogin()
        u_login.create(user)
        login_user(u_login)
        return redirect(url_for('shop'))
    else:
        data = ''
        if request.args.get('values') == 'True':
            data = 'Вы успешно зарегистрировались!'
        return render_template('login.html', form=form, data=data)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('shop'))


@app.route('/card/<uuid>')
def card_view(uuid: str):
    data = qdb.query_product_card(uuid)
    if data is None:
        return abort(404)
    return render_template('card.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
