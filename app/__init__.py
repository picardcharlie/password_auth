from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from flask_login import LoginManager

from . import main

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app(config_name = "default"):
    app = Flask(__name__)

    # import config settings
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #initilize extensions
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from app.models import db
    db.init_app(app)

    # register blueprints
    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    return app