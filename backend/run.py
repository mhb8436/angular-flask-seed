#!/usr/bin/env python
from server import app, db

if __name__ == "__main__":
	# print app
	# print app.config['SQLALCHEMY_DATABASE_URI']
	app.debug = True
	db.create_all(app=app)
	app.run(host='0.0.0.0',port=5001, debug=True)
