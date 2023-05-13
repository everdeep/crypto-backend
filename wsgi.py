from flask import abort
from tracker import TrackUsage
from tracker.storage.sql import SQLStorage

from app import create_app
from api.route import home_api, portfolio_api, data_api, user_api, admin_api

from sqlalchemy import create_engine

from config import app_config

ENGINE = create_engine(app_config.SQLALCHEMY_DATABASE_URI)


# Server config
DEBUG = True
MOCK = True

app = create_app()

# Track usage
t = TrackUsage(app, [SQLStorage(engine=ENGINE, table_name="server_activity")])


if __name__ == "__main__":
    t.include_blueprint(home_api)
    t.include_blueprint(portfolio_api)
    t.include_blueprint(data_api)
    t.include_blueprint(user_api)
    t.include_blueprint(admin_api)

    # Register blueprints
    app.register_blueprint(home_api, url_prefix="/api", name="home")
    app.register_blueprint(portfolio_api, url_prefix="/api/portfolio", name="portfolio")
    app.register_blueprint(data_api, url_prefix="/api/data", name="data")
    app.register_blueprint(user_api, url_prefix="/api/user", name="user")
    app.register_blueprint(admin_api, url_prefix="/api/admin", name="admin")

    @app.route("/", defaults={"u_path": ""})
    @app.route("/<path:u_path>")
    def catch_all(u_path):
        abort(404)
        # return render_template('index.html')

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5001, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app.run(debug=DEBUG, host="localhost", port=port)
