from flask.ext.testing import TestCase
from server import app, db

class BaseTestCase(TestCase):
	""" A base test case for wave """

	def create_app(self):
		app.config.from_object('config.TestConfiguration')
		return app
	
	def setUp(self):
		db.create_all()

	def tearDwon(self):
		db.session.remove()
		db.drop_all()	
