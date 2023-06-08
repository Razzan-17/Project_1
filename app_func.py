from init import db
from datetime import datetime
from models import Basket, Product, User
from hashlib import sha1
from sqlalchemy import func


class QueryDataBase:
    def add_product(self, product: str, user: str):
        '''Добавление товара в корзину пользователя'''
        bsk = Basket(users=user,
                     products=product)
        db.session.add(bsk)
        db.session.commit()

    def query_all(self):
        '''Запрос всех товаров в БД с ограничением в 18 карточек (Заглушка)'''
        data = db.session.execute(db.select(Product).limit(18)).scalars().all()
        return data

    def query_profile(self, email: str):
        '''Запрос данных и общей суммы для шаблона профиля раздел Корзина'''
        data = db.session.execute(db.select(Product).
                                  join_from(Basket, Product).
                                  join_from(Basket, User).
                                  filter(User.email == email)).scalars()
        summ = db.session.execute(db.select(func.sum(Product.price)).
                                  join_from(Basket, Product).
                                  join_from(Basket, User).
                                  filter(User.email == email)).scalars()
        return data, summ

    def query_product_card(self, uuid):
        '''Запрос данных для карточек'''
        data = db.session.execute(db.select(Product).
                                  filter(Product.uuid == uuid)).scalars().first()
        return data

    def create_user(self, psw, form):
        '''Создание нового пользователя'''
        hash_psw = hash_password(psw)
        user = User(name=form.get('name'),
                    email=form.get('email'),
                    password=hash_psw,
                    date=datetime.utcnow().strftime('%d.%m.%Y'))
        db.session.add(user)
        db.session.commit()


def hash_password(psw: str):
    '''Хеширование пароля'''
    return sha1(bytes(psw, 'utf-8')).hexdigest()

