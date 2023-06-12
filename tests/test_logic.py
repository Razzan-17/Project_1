import pytest

from init import create_app
from conf import URI_test
from app_func import QueryDataBase as qdb

class TestViewsPost:
    def setup(self):
        app = create_app(URI_test)
        app.testing = True
        self.client = app.test_client()

    def login(self, email: str, psw: str):
        return self.client.post('/login', data={
            'email': email,
            'password': psw},
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_register(self):
        form = {'name': 'Test',
                'email': 'test@test.ru'}
        qdb.create_user('123123123', form)
        response = self.login(form['email'], '123123123')
        assert response.status_code == 200

    @pytest.mark.parametrize('email', ['test1@test.ru', 'test@test', ''])
    def test_login_email(self, email):
        response = self.login(email, '123123123')
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