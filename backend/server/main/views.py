from flask import abort, Blueprint, flash, redirect, render_template, request, url_for, g
from flask.ext.login import login_required, login_user, logout_user,current_user
import urllib
from server.main.models import *
from server.util import *
from server.users.views import auth
import simplejson as json
from server.data import query_to_list_json

main = Blueprint("main", __name__)


@main.route("/menu", methods=['GET','POST','OPTIONS'])
@crossdomain(origin='http://localhost:8888', credentials=True, headers='Authorization')
@auth.login_required
def list_menu():
	userid = g.user.id
	query = Menu.query.filter(Menu.id==MenuUser.menuid).filter(MenuUser.userid==userid)
	data = query_to_list_json(query)
	return json.dumps(data)

@main.route("/", methods=("GET","POST"))
def index():
	return jsonify({'index':''})