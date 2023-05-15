from http import HTTPStatus
from flask import Blueprint, request
from flask_login import login_required, current_user

from api.service import UserService, DataService
from cryptolib.schema import (
    UserSchema,
    CurrencyPairConfigSchema,
    PortfolioSchema,
    OrderSchema,
)
from cryptolib.utils import get_unfiltered_response

admin_api = Blueprint("api", __name__)


@admin_api.route("/users")
@login_required
def get_all_users():
    """
    Returns all users
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = UserService().get_all_users()
    schema_result = UserSchema().dump(result, many=True)

    # Merge the two results
    return [get_unfiltered_response(a, b) for a, b in zip(result, schema_result)], 200


@admin_api.route("/users/<user_id>")
@login_required
def get_user(user_id):
    """
    Returns a user
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    print("user_id: ", user_id)

    result = UserService().get_user(user_id)
    schema_result = UserSchema().dump(result)
    return get_unfiltered_response(result, schema_result), 200


@admin_api.route("/users/<user_id>/portfolio")
@login_required
def get_user_portfolio(user_id):
    """
    Returns a user's portfolio
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().get_portfolio(user_id)
    schema_result = PortfolioSchema().dump(result)
    return get_unfiltered_response(result, schema_result), 200


@admin_api.route("/users/<user_id>/portfolio", methods=["POST"])
@login_required
def update_user_portfolio(user_id):
    """
    Updates a user's portfolio
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().update_portfolio(user_id, request.get_json())
    schema_result = PortfolioSchema().dump(result)
    return get_unfiltered_response(result, schema_result), 200


@admin_api.route("/users/<user_id>/<currency_pair>/config")
@login_required
def get_user_portfolio_currency_pair_config(user_id, currency_pair):
    """
    Returns a user's portfolio
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().get_currency_pair_config(user_id, currency_pair)
    schema_result = CurrencyPairConfigSchema().dump(result)
    return get_unfiltered_response(result, schema_result), 200


@admin_api.route("/users/<user_id>/portfolio/<currency_pair>/config", methods=["POST"])
@login_required
def update_user_portfolio_currency_pair_config(user_id, currency_pair):
    """
    Updates a user's portfolio
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().update_currency_pair_config(user_id, currency_pair)
    return CurrencyPairConfigSchema().dump(result), 200


# Get all orders
@admin_api.route("/orders")
@login_required
def get_all_orders():
    """
    Returns all orders
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().get_all_orders()
    return OrderSchema().dump(result), 200


# Get all orders for a user
@admin_api.route("/orders/<user_id>")
@login_required
def get_user_orders(user_id):
    """
    Returns all orders for a user
    ---
    """
    # check if the user is an admin
    if not current_user.is_admin:
        return {"error": "You are not authorized to perform this action"}, 403

    result = DataService().get_all_user_orders(user_id)
    return OrderSchema().dump(result), 200
