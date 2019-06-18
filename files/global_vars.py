from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app as app

class global_variables():
    def __init__(self):
        self.db=SQLAlchemy(app)
        self.migrate = Migrate(app, self.db)