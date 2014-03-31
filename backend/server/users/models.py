import server
import os
from flask.ext.login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from passlib.apps import custom_app_context as pwd_context
from server.data import CRUDMixin, db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

class User(UserMixin, CRUDMixin, db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String)
	email = db.Column(db.String)
	pwd  = db.Column(db.String)

	@hybrid_property
	def password(self):
		return self.pwd

	@password.setter
	def password(self, password):
		self.pwd = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.pwd)

	def generate_auth_token(self, expiration = 12000):
		s = Serializer(server.app.config['SECRET_KEY'], expires_in = expiration)
		return s.dumps({'id':self.id})

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(server.app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None
		except BadSignature:
			return None
		user = User.query.filter_by(id=data['id']).first()
		return user

	def __repr__(self):
		return "<User #{0} {1} ".format(self.id, self.name)

