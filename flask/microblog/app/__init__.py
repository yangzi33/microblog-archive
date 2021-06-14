from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Note: to initiaize db for the first time, run `flask db init` at basedir
db = SQLAlchemy(app)

# To migrate, run `flask db migrate -m "<message>"`, followed by `flask db upgrade`
# for migration update
migrate = Migrate(app, db)

# For User login (form chapter 4)
login = LoginManager(app)
login.login_view = "login"

from app import routes, models