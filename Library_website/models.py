from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timedelta

# Class defining the books
class Book(db.Model):
    __tablename__ = 'books_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    date_lent = db.Column(db.DateTime(timezone=True), default=func.now())
    num_of_copies = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Class defining the users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    books = db.relationship('Book', lazy=True)


 



