from flask import Flask
from config import config_init
from db import db
from todo.router import tasks_route
import cli

def create_app():
    app = Flask(__name__)
    config_init(app)
    db.init_app(app)
    cli.init_cli(app)
    app.register_blueprint(tasks_route)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()


