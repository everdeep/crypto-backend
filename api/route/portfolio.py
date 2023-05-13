from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from flask_login import login_required, current_user

from api.schema import PortfolioSchema
from api.service import PortfolioService

portfolio_api = Blueprint("api", __name__)


@portfolio_api.route("/earnings", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {"description": "Returns the earnings of the user"}
        }
    }
)
def getEarnings():
    """
    Returns the earnings of the user
    ---
    """
    result = PortfolioService().get_earnings(current_user.id)
    if result is None:
        return {"error": "No portfolio found for user"}, 404

    return jsonify(result), 200
