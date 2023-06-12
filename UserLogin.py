from models import Buyer
from flask_login import UserMixin


class UserLogin(UserMixin):
    def __init__(self, *args):
        self._user = None
        super().__init__(*args)

    def fromDB(self, user_email):
        self._user = Buyer.query.filter(Buyer.email == user_email).first()
        return self

    def create(self, user=None):
        self._user = user

    def get_id(self):
        return str(self._user.email)

    def get_prof(self):
        return self._user
