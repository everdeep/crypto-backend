from flask import Flask, abort
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flasgger import Swagger
from flask_mail import Mail

from http import HTTPStatus

from config import app_config

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
mail = Mail()


def create_app():
    app = Flask(__name__, template_folder="templates")

    ## Initialize CORS
    CORS(app, supports_credentials=True)

    ## Initialize Config
    app.config.from_object(app_config)
    app.config["SWAGGER"] = {"title": "Crypto API", "uiversion": 3}
    swagger = Swagger(app)

    # Order matters here
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    # Setup session management
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    from api.model import UserModel

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        abort(HTTPStatus.UNAUTHORIZED)
        # return {'error': 'Unauthorised access'}, 401

    return app


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(debug=True, host="0.0.0.0", port=port)
