from datetime import datetime
from uuid import uuid1
from __init__py import db


class User(db.Model):
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(24), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    basket = db.relationship('Basket', backref='user', lazy='dynamic')
    like = db.relationship('Like', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return self.name


class Product(db.Model):
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo_name = db.Column(db.String(50), nullable=False, unique=True)
    uuid = db.Column(db.String(90), nullable=False, default=str(uuid1()), unique=True, primary_key=True)
    basket = db.relationship('Basket', backref='product', lazy='dynamic')
    like = db.relationship('Like', backref='product', lazy='dynamic')
    comment = db.relationship('Comment', backref='product', lazy='dynamic')

    def __repr__(self):
        return f'{self.name}: {self.price}'


class Basket(db.Model):
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)
    count = db.Column(db.Integer, default=0)


class Like(db.Model):
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)


class Comment(db.Model):
    users = db.Column(db.String(30), db.ForeignKey('user.email'), primary_key=True)
    products = db.Column(db.String(30), db.ForeignKey('product.uuid'), primary_key=True)
    text = db.Column(db.String(250), default='', nullable=True)
    date = db.Column(db.String(50), default=datetime.utcnow().strftime('%d.%m.%Y %H:%M'))

    def __repr__(self):
        return f'{self.text} ({self.date})'
