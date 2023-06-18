import pytest


@pytest.mark.usefixtures('create_client')
class TestViewsGet:
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
