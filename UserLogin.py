from models import User


class UserLogin:
    def fromDB(self, user_email):
        self.__user = User.query.filter(User.email == user_email).first()
        return self

    def create(self, user):
        print(user)
        self.__user = user

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['email'])
