from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(64), unique = True, index = True)
    pasword_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("don't look at this!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password):
        self.username = username
        self.password = password