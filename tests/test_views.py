import pytest
from conf import URI_test
from app import app


class TestViewsGet:
    def setup(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = URI_test
        app.testing = True
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
