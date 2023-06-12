from init import db


class Buyer(db.Model):
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    basket = db.relationship('Basket', backref='buyer', lazy='dynamic')

    def __repr__(self):
        return self.name


class Product(db.Model):
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo_name = db.Column(db.String(50), nullable=False, unique=True)
    uuid = db.Column(db.String(90), nullable=False, unique=True, primary_key=True)
    basket = db.relationship('Basket', backref='product', lazy='dynamic')

    def __repr__(self):
        return f'{self.name}- {self.price}'


class Basket(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    users = db.Column(db.String(120), db.ForeignKey('buyer.email'))
    products = db.Column(db.String(90), db.ForeignKey('product.uuid'))
    count = db.Column(db.Integer, default=1)
