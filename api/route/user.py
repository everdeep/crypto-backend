from datetime import timedelta
from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_login import login_user, logout_user, login_required, current_user
from api.service import UserService
from cryptolib.schema import UserSchema, UserSettingsSchema, UserActivitySchema
from cryptolib.utils import generate_password

user_api = Blueprint("api", __name__)


# Delete user
@user_api.route("/", methods=["DELETE"])
@login_required
@swag_from({"responses": {HTTPStatus.OK.value: {"description": "Delete user"}}})
def delete_user():
    """
    Deletes the user
    ---
    """
    result = UserService().delete_user(current_user.id)
    if not result:
        return {"error": "Failed to delete user"}, 400

    return {"success": True}, 200


@user_api.route("/activity", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Gets current users activity",
                "schema": UserSchema,
            }
        }
    }
)
def get_activity():
    """
    Gets the current users activity
    ---
    """
    action = request.args.get("action")
    activity = UserService().get_activity(current_user.id, action)
    return UserActivitySchema().dump(activity, many=True), 200


@user_api.route("/details", methods=["POST"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Updates current user",
                "schema": UserSchema,
            }
        }
    }
)
def update_user_details():
    """
    Updates the current users details
    ---
    """
    request_data = request.get_json()
    result = UserService().update_user_details(current_user.id, request_data)
    if not result:
        return {"error": "Failed to update user"}, 400

    print(UserSchema().dump(result))
    return UserSchema().dump(result), 200


@user_api.route("/password", methods=["POST"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Updates current users password",
                "schema": UserSchema,
            }
        }
    }
)
def update_user_password():
    """
    Updates the current users password
    ---
    """
    request_data = request.get_json()
    result = UserService().update_user_password(
        current_user.id, request_data.get("password")
    )
    if not result:
        return {"error": "Failed to update user"}, 400

    return UserSchema().dump(result), 200


# Check if the user is logged in
@user_api.route("/login", methods=["GET"])
def is_logged_in():
    """
    Checks if the user is logged in
    ---
    """

    if current_user.is_authenticated:
        print(current_user)
        return {"loggedIn": True, "user": UserSchema().dump(current_user)}, 200

    return {"loggedIn": False}, 200


@user_api.route("/login", methods=["POST"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {"description": "Login route", "schema": UserSchema}
        }
    }
)
def login():
    """
    Logs the user in
    ---
    """

    request_data = request.get_json()
    user = UserService().login(request_data["username"], request_data["password"])
    if not user:
        return {"error": "Invalid credentials"}, 400

    # Timeout the session after 30 seconds
    login_user(user, remember=True, duration=timedelta(seconds=10))

    return UserSchema().dump(user), 200


@user_api.route("/google-login", methods=["POST"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Login route for Google",
                "schema": UserSchema,
            }
        }
    }
)
def loginGoogle():
    """
    Logs the user in
    ---
    """

    code = request.get_json().get("code")
    if not code:
        return {"error": "Invalid credentials"}, 400

    profile = UserService().loginGoogle(code)
    if not profile:
        return {"error": "Invalid credentials"}, 400

    user = UserService().get_user(profile["email"])
    if not user:
        # Register the user
        password = generate_password()
        user = UserService().register(
            {
                "email": profile.get("email"),
                "password": password,
                "first_name": profile.get("given_name"),
                "last_name": profile.get("family_name"),
            },
            authType="v2",
        )

        if not user:
            return {"error": "Failed to create user"}, 400

    login_user(user, remember=True)

    return UserSchema().dump(user), 200


@user_api.route("/logout")
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {"description": "Logout route", "schema": UserSchema}
        }
    }
)
def logout():
    """
    Logs the user out
    ---
    """

    logout_user()
    return [], 200


@user_api.route("/register", methods=["POST"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {"description": "Register route", "schema": UserSchema}
        }
    }
)
def register():
    """
    Registers the user
    ---
    """

    request_data = request.get_json()
    result = UserService().register(
        {
            "email": request_data.get("email"),
            "password": request_data.get("password"),
            "first_name": request_data.get("first_name"),
            "last_name": request_data.get("last_name"),
        },
    )

    if not result:
        return {"error": "Email already exists"}, 400

    return UserSchema().dump(result), 200


# Get user settings
@user_api.route("/settings", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Get user settings",
                "schema": UserSchema,
            }
        }
    }
)
def get_settings():
    """
    Gets the user settings
    ---
    """
    result = UserService().get_settings(current_user.id)
    return [UserSettingsSchema().dump(i) for i in result], 200


# Get the user role
@user_api.route("/role", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {"description": "Get user role", "schema": UserSchema}
        }
    }
)
def get_role():
    """
    Gets the user role
    ---
    """
    result = UserService().get_role(current_user.id)
    return jsonify(result), 200
