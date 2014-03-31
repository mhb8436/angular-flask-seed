from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import expression
from sqlalchemy.ext import compiler
from sqlalchemy import desc
from collections import OrderedDict

db = SQLAlchemy()

class CRUDMixin(object):

	@classmethod
	def create(cls, commit=True, **kwargs):
		print 'create------'
		instance = cls(**kwargs)
		for k, v in kwargs.iteritems():
			print "%s = %s" % (k,v)
		return instance.save(commit=commit)

	@classmethod
	def get(cls, id):
		return cls.query.get(id)

	@classmethod
	def get_or_404(cls, id):
		return cls.query.get_or_404(id)

	def update(self, commit=True, **kwargs):
		for attr, value in kwargs.iteritems():
			setattr(self, attr, value)
		return commit and self.save() or self

	def save(self, commit=True):
		db.session.add(self)
		if commit:
			db.session.commit()
		return self

	def delete(self,commit=True):
		db.session.delete(self)
		return commit and db.session.commit()


def query_to_list_json(query):
	datas = []
	results = db.session.execute(query)

	for row in list(results):
		rowdict = OrderedDict() 
		c = 0
		keys = results.keys()[:]
		for key in results.keys():
			c += 1
			nKey = str(key).split('_')
			if '_' in str(key):
				rowdict.update({nKey[1]:row[key]})
			else:
				rowdict.update({key:row[key]})
		datas.append(rowdict)
	
	return datas


class group_concat(expression.FunctionElement):
	name = "group_concat"


