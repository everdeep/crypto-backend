from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.schema.welcome import WelcomeSchema
from api.service.welcome import WelcomeService

home_api = Blueprint("api", __name__)


@home_api.route("/")
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Welcome to the Flask Starter Kit",
                "schema": WelcomeSchema,
            }
        }
    }
)
def welcome():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    result = WelcomeService().get_welcome()
    return WelcomeSchema().dump(result), 200
