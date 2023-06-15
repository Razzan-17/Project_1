from init import db
from datetime import datetime
from models import Basket, Product, Buyer
from hashlib import sha1
from sqlalchemy import func


class QueryDataBase:
    @staticmethod
    def check_basket(user: str, product: str):
        '''проверка есть ли продукт в корзине пользователя'''
        data = db.session.execute(db.select(Basket).
                                  filter(Basket.users == user)).scalars().all()
        for prod in data:
            if prod.products == product:
                return True
        return False

    @staticmethod
    def add_product(product: str, user: str):
        '''Добавление товара в корзину пользователя'''
        bsk = Basket(users=user,
                     products=product)
        db.session.add(bsk)
        db.session.commit()

    @staticmethod
    def del_product(product: str, user: str):
        '''Удаление товара из корзины пользователя'''
        db.session.execute(db.select(Basket).
                           filter(Basket.users == user).
                           filter(Basket.products == product)).scalar().delete()
        db.session.commit()

    @staticmethod
    def query_all():
        '''Запрос всех товаров в БД с ограничением в 18 карточек (Заглушка)'''
        data = db.session.execute(db.select(Product).limit(18)).scalars().all()
        return data

    @staticmethod
    def query_profile(email: str):
        '''Запрос данных и общей суммы для шаблона профиля раздел Корзина'''
        data = db.session.execute(db.select(Product).
                                  join_from(Basket, Product).
                                  join_from(Basket, Buyer).
                                  filter(Buyer.email == email)).scalars()
        summ = db.session.execute(db.select(func.sum(Product.price)).
                                  join_from(Basket, Product).
                                  join_from(Basket, Buyer).
                                  filter(Buyer.email == email)).scalars()
        return data, summ

    @staticmethod
    def query_product_card(uuid: str):
        '''Запрос данных для карточек'''
        data = db.session.execute(db.select(Product).
                                  filter(Product.uuid == uuid)).scalars().all()
        return data

    @staticmethod
    def check_user(form):
        '''Проверка существования email при регистрации'''
        return Buyer.query.filter(Buyer.email == form['email']).first()

    @staticmethod
    def create_user(psw: str, form):
        '''Создание нового пользователя'''
        hash_psw = hash_password(psw)
        user = Buyer(name=form.get('name'),
                     email=form.get('email'),
                     password=hash_psw,
                     date=datetime.utcnow().strftime('%d.%m.%Y'))
        db.session.add(user)
        db.session.commit()


def hash_password(psw: str):
    '''Хеширование пароля'''
    return sha1(bytes(psw, 'utf-8')).hexdigest()

