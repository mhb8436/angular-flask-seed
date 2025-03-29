from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_security import Security
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
security = Security()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    security.init_app(app)
    CORS(app)
    
    # Register blueprints
    from .users import bp as users_bp
    from .main import bp as main_bp
    
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(main_bp, url_prefix='/api/main')
    
    return app
