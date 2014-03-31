from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from server.data import db, CRUDMixin

import sys
import simplejson as json

from server.users.models import User
from sqlalchemy.sql import text, exists, and_, or_, not_, func, operators, literal_column, union_all, distinct
from sqlalchemy.sql import tuple_
from sqlalchemy import cast, select, String



class Menu(CRUDMixin, db.Model):
	__tablename__ = 'menu'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	leafyn = db.Column(db.String)
	groupid = db.Column(db.Integer)

	def __repr__(self):
		return '<Menus {0} {1} {2}>'.format(self.id, self.groupid, self.name)

class MenuUser(CRUDMixin, db.Model):
	__tablename__ = 'menuuser'

	menuid = db.Column(db.Integer, primary_key=True)
	userid = db.Column(db.Integer, primary_key=True)

	def __repr__(self):
		return '<MenusUser {0} {1} {2}>'.format(self.userid, self.menuid)
		
