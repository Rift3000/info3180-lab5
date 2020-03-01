from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatPassword?"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:superuser@localhost/Lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

username = "Thriller"  #Not wise as far as security is concerned but I simply wanted to state the username
password = "cakesoap"  #And the password I used for my database
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
