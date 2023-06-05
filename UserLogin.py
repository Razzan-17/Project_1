from models import User
from flask_login import UserMixin


class UserLogin(UserMixin):
    def fromDB(self, user_email):
        self._user = User.query.filter(User.email == user_email).first()
        return self

    def create(self, user=None):
        self._user = user

    def get_id(self):
        return str(self._user.email)

    def get_prof(self):
        return self._user
