import os
import requests
from api.model import UserModel
from api.model import (
    UserSettingsModel,
    ServerActivityModel,
    AddressModel,
    PortfolioModel,
)

from api.service.email import EmailService
from cryptolib.enums import UserActions
from app import db, bcrypt


class UserService:
    def get_activity(self, user_id, action=None):
        if action:
            try:
                endpoint = UserActions[action].value
                return (
                    ServerActivityModel.query.filter_by(
                        user_id=user_id, endpoint=endpoint
                    )
                    .order_by(ServerActivityModel.id.desc())
                    .all()
                )
            except KeyError:
                return None

        return (
            ServerActivityModel.query.filter_by(user_id=user_id)
            .order_by(ServerActivityModel.id.desc())
            .all()
        )

    def get_user(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            return user
        return False

    def get_all_users(self):
        users = UserModel.query.all()
        return users

    #
    # TODO - update user details
    #
    def update_user_details(self, user_id, user_details):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            user.first_name = (
                user_details.get("firstName")
                if user_details.get("firstName")
                else user.first_name
            )
            user.last_name = (
                user_details.get("lastName")
                if user_details.get("lastName")
                else user.last_name
            )
            user.email = (
                user_details.get("email") if user_details.get("email") else user.email
            )
            user.username = (
                user_details.get("username")
                if user_details.get("username")
                else user.username
            )
            user.phone = (
                user_details.get("phoneNumber")
                if user_details.get("phoneNumber")
                else user.phone
            )
            user.dob = user_details.get("dob") if user_details.get("dob") else user.dob

            db.session.commit()
            return user

        return None

    def update_user_password(self, user_id, password):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            user.password = password
            db.session.commit()
            return user

        return None

    # login user
    def login(self, username, password):
        user = UserModel.query.filter_by(email=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        return None

    # login user with google
    def loginGoogle(self, code):
        url = "https://accounts.google.com/o/oauth2/token"
        data = {
            "code": code,
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
            "redirect_uri": os.environ.get("REDIRECT_URI"),
            "grant_type": "authorization_code",
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        token_response = requests.post(url, data=data, headers=headers)
        print(data)
        print(token_response)
        if token_response.status_code != 200:
            return None

        access_token = token_response.json()["access_token"]
        url = (
            f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={access_token}"
        )
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        }
        profile = requests.get(url, headers=headers)
        if profile.status_code == 200:
            return profile.json()

        return None

    # register user
    def register(self, user_details, authType="local"):
        user = UserModel.query.filter_by(email=user_details.get("email")).first()
        if user:
            return None

        user = UserModel(**user_details)
        db.session.add(user)
        db.session.flush()

        # Create portfolio
        portfolio = PortfolioModel()
        portfolio.user_id = user.id
        db.session.add(portfolio)

        # Create address
        address = AddressModel()
        db.session.add(address)

        db.session.flush()

        user.portfolio_id = portfolio.id
        user.address_id = address.id

        db.session.commit()

        # Send welcome email
        template = "email/welcome-local"
        context = {"name": f"{user.first_name} {user.last_name}"}
        if authType == "v2":
            template = "email/welcome-v2"
            context["password"] = user_details.get("password")

        EmailService().send_email(
            "Welcome to Mimic", template, recipients=[user.email], context=context
        )

        return user

    # get user settings
    def get_settings(self, user_id):
        settings = UserSettingsModel.query.filter_by(user_id=user_id).all()
        return settings

    # get user role
    def get_role(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            return user.role

        return None

    def delete_user(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            # address = user.address
            # if address:
            #     db.session.delete(address)

            # portfolio = user.portfolio
            # if portfolio:
            #     db.session.delete(portfolio)

            # currency_configs = CurrencyPairConfigModel.query.filter_by(user_id=user_id).all()
            # for config in currency_configs:
            #     signal = config.signal
            #     db.session.delete(signal)
            #     db.session.delete(config)

            db.session.delete(user)
            db.session.commit()
            return True

        return False
