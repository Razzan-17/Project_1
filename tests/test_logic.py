import pytest

from app import app
from conf import URI_test
from init import db
from models import Buyer


class TestViewsPost:
    def setup(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = URI_test
        self.client = app.test_client()
        Buyer.query.delete()
        db.session.commit()

    def login(self, email: str, psw: str):
        return self.client.post('/login', data={
            'email': email,
            'password': psw},
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_register(self):
        form = {'name': 'Test',
                'email': 'test@test.ru',
                'password': '123123123',
                'confirm': '123123123'}
        response = self.client.post('/register', data=form, follow_redirects=True)
        assert response.status_code == 200, 'Ошибка доступа к странице регистрации'
        assert 'Вы успешно зарегистрировались!' in response.text, 'Ошибка редиректа при регистрации'
        response = self.login(form['email'], form['password'])
        assert response.status_code == 200, 'Ощибка авторизации после регистрации'
        db.session.commit()

    @pytest.mark.parametrize('email', ['test1@test.ru', 'test@test', ''])
    def test_login_email(self, email):
        response = self.login(email, '11111111')
        assert response.status_code == 200
        assert 'Вы не зарегистрированы' in response.text

    @pytest.mark.parametrize('password', ['1231231231', 'test', ''])
    def test_login_password(self, password):
        response = self.login('test@test.ru', password)
        assert response.status_code == 200
        assert 'Неверный пароль' in response.text

    def test_login_logout(self):
        self.login('test@test.ru', '123123123')
        response = self.logout()
        assert response.status_code == 200


#register
#login
#profile

#add_product
#query_all
#query_profile
#query_product_card
#hash_password
#create_user