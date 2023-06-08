import os

import pytest
from tempfile import mkstemp
from app import app
from init import db


app.testing = True


class TestViewsGet:
    def setup(self):
        self.client = app.test_client()

    @pytest.mark.parametrize('address', ['/', '/login', '/register'])
    def test_code_200(self, address):
        resp = self.client.get(address)
        assert resp.status_code == 200

    @pytest.mark.parametrize('address', ['/profile', '/logout'])
    def test_code_401(self, address):
        resp = self.client.get(address)
        assert resp.status_code == 401

    @pytest.mark.parametrize('address', ['123456789', 'aa2dd1123', ''])
    def test_code_404(self, address):
        resp = self.client.get('/card/' + address)
        assert resp.status_code == 404


class TestViewsPost:
    def setup(self):
        self.db_fd, app.config['SQLALCHEMY_DATABASE_URI'] = mkstemp()
        self.client = app.test_client()
        db.create_all()

    def teardown(self):
        os.close(self.db_fd)
        os.unlink(app.config['SQLALCHEMY_DATABASE_URI'])

    def test_login_logout(self):
        d = {'email': 'eee@ee.ee', 'password': '123123123'}
        self.client.post('/login', data=d, follow_redirects=True)
        res = self.client.get('/logout', follow_redirects=True)
        assert res.status_code == 200


#register
#login
#profile

#add_product
#query_all
#query_profile
#query_product_card
#hash_password
#create_user