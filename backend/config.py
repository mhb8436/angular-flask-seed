import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
	# Flask Configuration
	ENV = os.environ.get('FLASK_ENV', 'production')
	DEBUG = os.environ.get('FLASK_DEBUG', '0') == '1'
	PORT = int(os.environ.get('PORT', 5000))
	
	# Security
	SECRET_KEY = os.environ.get('SECRET_KEY')
	if not SECRET_KEY:
		raise ValueError("No SECRET_KEY set for Flask application")
	
	SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
	if not SECURITY_PASSWORD_SALT:
		raise ValueError("No SECURITY_PASSWORD_SALT set for Flask application")
	
	# Database
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	if not SQLALCHEMY_DATABASE_URI:
		raise ValueError("No DATABASE_URL set for Flask application")
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# Security settings
	SECURITY_REGISTERABLE = True
	SECURITY_SEND_REGISTER_EMAIL = False
	SECURITY_UNAUTHORIZED_VIEW = None
	SESSION_COOKIE_SECURE = True  # Only send cookies over HTTPS
	REMEMBER_COOKIE_SECURE = True
	SESSION_COOKIE_HTTPONLY = True
	REMEMBER_COOKIE_HTTPONLY = True
	
	# CORS settings
	CORS_ORIGINS = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:4200').split(',')
