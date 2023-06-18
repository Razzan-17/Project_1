import pytest
from models import Buyer
from app import app
from conf import URI_test
from init import db


@pytest.fixture()
def create_client(request, delete_user):
    app.config['SQLALCHEMY_DATABASE_URI'] = URI_test
    app.testing = True
    app.debug = True
    request.cls.client = app.test_client()


@pytest.fixture()
def delete_user():
    yield
    user = db.session.execute(db.select(Buyer).filter(Buyer.email == 'test@test.ru')).scalar()
    if user:
        db.session.delete(user)
        db.session.commit()


@pytest.fixture()
def create_user(delete_user):
    user = Buyer(name='Test',
                 email='test@test.ru',
                 password='88ea39439e74fa27c09a4fc0bc8ebe6d00978392',
                 date='test date')
    db.session.add(user)
    db.session.commit()
    yield
