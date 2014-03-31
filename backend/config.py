from os.path import abspath, dirname, join
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfiguration(object):
	DEBUG = False
	TESTING = False
	# SERVER_NAME = 'localhost'
	ADMINS = frozenset(['mhb8436@gmail.com'])
	SECRET_KEY = 'flask-session-insecure-secret-key'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_ECHO = True

class TestConfiguration(BaseConfiguration):
	DEBUG = True
	TESTING = True
	CSRF_ENABLED = True
	SQLALCHEMY_ECHO = True
