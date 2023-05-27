from datetime import datetime
from uuid import uuid4

from app import db


class User(db.Model):
    __nametable__ = 'users'
    name = db.Column(db.String(30))
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String())
    basket = db.relationship('Basket', backref='user', lazy='dynamic')
    like = db.relationship('Like', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return self.name


class Product(db.Model):
    __nametable__ = 'products'
    name = db.Column(db.String(30))
    description = db.Column(db.String(250))
    price = db.Column(db.Integer)
    photo_name = db.Column(db.String(50))
    uuid = db.Column(db.String(30), primery_key=True)
    basket = db.relationship('Basket', backref='product', lazy='dynamic')
    like = db.relationship('Like', backref='product', lazy='dynamic')
    comment = db.relationship('Comment', backref='product', lazy='dynamic')

    def __init__(self, name, description, price, foto, uuid=None):
        self.name = name
        self.description = description
        self.price = price
        self.foto = foto
        if uuid is None:
            uuid = uuid4()
        self.uuid = uuid

    def __repr__(self):
        return f'{self.name}: {self.price}'


class Basket(db.Model):
    __nametable__ = 'baskets'
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self, users, products, count):
        self.users = users
        self.products = products
        self.count = count


class Like(db.Model):
    __nametable__ = 'likes'
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)

    def __init__(self, users, products):
        self.users = users
        self.products = products


class Comment(db.Model):
    __nametable__ = 'comments'
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)
    text = db.Column(db.String(250))
    date = db.Column(db.String(50))

    def __init__(self, users, products, text, date=None):
        self.users = users
        self.products = products
        self.text = text
        if date is None:
            date = datetime.utcnow()
        self.date = date

    def __repr__(self):
        return f'{self.text ({self.date})}'
