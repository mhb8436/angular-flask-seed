from flask import Flask
from .auth import login_manager
from .data import db
from .users.views import users
from .main.views import main

app = Flask(__name__)
app.config.from_object('config.TestConfiguration')

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(users, url_prefix='/api/v1.0/users')
app.register_blueprint(main, url_prefix='/api/v1.0/main')
