import pytest

from app_func import hash_password, QueryDataBase as qdb


class TestFunc:
    @pytest.mark.parametrize('psw, psw_hash',
                             [('11111111', 'a642a77abd7d4f51bf9226ceaf891fcbb5b299b8'),
                              ('2', 'da4b9237bacccdf19c0760cab7aec4a8359010b0'),
                              (54, '80e28a51cbc26fa4bd34938c5e593b36146f5e0c')])
    def test_hash_password(self, psw, psw_hash):
        password_hash = hash_password(psw)
        assert psw_hash == password_hash

    @pytest.mark.parametrize('psw', [12345, 'acc', 'a', 'ab!lfjcZ14812381891jcj.ahdu**d'])
    def test_len_hash_password(self, psw):
        assert len(hash_password(psw)) == 40

    def test_none_hash_password(self):
        assert hash_password('') is None