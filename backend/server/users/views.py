from flask import url_for, abort, Blueprint, flash, redirect, render_template, request, g
from flask.ext.login import login_required, login_user, logout_user,current_user
from flask import jsonify
from flask.ext.httpauth import HTTPBasicAuth

from .models import User
from server.util import *

users = Blueprint("users", __name__, template_folder='templates')
auth = HTTPBasicAuth()
TOKEN_DURATION = 12000

@users.route("/login/", methods=["GET","POST"])
@crossdomain(origin='http://localhost:8888', credentials=True, headers='Authorization')
def login():
	email = request.json.get('email')
	password = request.json.get('password')
	user = User.query.filter_by(email=email).first()
	if user.verify_password(password):
		login_user(user)
	return jsonify({'name':user.name}), 201, {'Location':url_for('users.get_user', id = user.id, _external=True)}


@auth.verify_password
def verfiy_password(email_or_token, password):
	user = User.verify_auth_token(email_or_token)
	if not user:
		user = User.query.filter_by(email=email_or_token).first()
		if not user or not user.verify_password(password):
			return False
	g.user = user
	login_user(user)
	return True	

@users.route("/register", methods=['POST'])
def register():
	email = request.json.get('email')
	password = request.json.get('password')
	name = request.json.get('name')

	if name is None or password is None or email is None:
		abort(400)
	if User.query.filter(User.email==email).first() is not None:
		abort(400)

	user = User.create(**dict(zip(('email','name','password'),(email, name, password))))
	return jsonify({ 'name': user.name }), 201, {'Location':url_for('users.get_user', id=user.id, _method='GET')}

@users.route('/id/<int:id>', methods=['GET','POST'])
def get_user(id):
	print 'get_user id is ' + str(id)
	user = User.query.filter_by(id=id).first()
	if not user:
		abort(400)
	return jsonify({ 'name': user.name })

@users.route('/token', methods=['GET','POST','OPTIONS'])
@crossdomain(origin='http://localhost:8888', credentials=True, headers='Authorization')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(TOKEN_DURATION)
    return jsonify({ 'token': token.decode('ascii'), 'duration': TOKEN_DURATION })

@users.route('/test/resource')
@crossdomain(origin='http://localhost:8888', credentials=True, headers='Authorization')
@auth.login_required
def get_resource():
	return jsonify({'data':'Hello, %s' % g.user.id})


