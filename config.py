import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "hello_world"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

config = {'default': Config}