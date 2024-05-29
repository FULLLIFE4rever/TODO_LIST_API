from db import db
from todo import models  # noqa


def init_cli(app):
    @app.cli.command()
    def create_db():
        """Create tables in database"""
        db.create_all()
