import pytest


@pytest.mark.usefixtures('create_client')
class TestViewsPost:
    def login(self, email: str, psw: str):
        return self.client.post('/login', data={
            'email': email,
            'password': psw},
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_register(self, delete_user):
        form = {'name': 'Test',
                'email': 'test@test.ru',
                'password': '123123123',
                'confirm': '123123123'}
        response = self.client.post('/register', data=form, follow_redirects=True)
        assert response.status_code == 200, 'Ошибка доступа к странице регистрации'
        assert 'Вы успешно зарегистрировались!' in response.text, 'Ошибка редиректа при регистрации'
        response = self.login(form['email'], form['password'])
        assert response.status_code == 200, 'Ошибка авторизации после регистрации'

    @pytest.mark.parametrize('email', ['test1@test.ru', 'test@test'])
    def test_login_email(self, email):
        response = self.login(email, '111111111')
        assert response.status_code == 200
        assert 'Вы не зарегистрированы' in response.text

    @pytest.mark.parametrize('password', ['1231231231', 'test12341'])
    def test_login_password(self, password, create_user):
        response = self.login('test@test.ru', password)
        assert response.status_code == 200
        assert 'Неверный пароль' in response.text

    def test_login_logout(self, create_user):
        self.login('test@test.ru', '123123123')
        response = self.logout()
        assert response.status_code == 200
