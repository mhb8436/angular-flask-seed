import sys
sys.path.append("/Users/airplug/git/mhb8436.github.io/flask-angular-seed/backend/") # your absolute directory 

from flask import abort, Blueprint, flash, jsonify, Markup, redirect, render_template, request, url_for, g
from bases import BaseTestCase
import simplejson as json
from base64 import b64encode

class TestView(BaseTestCase):


	# if you want to test other view, you must copy this method and then test it 
	def test_menu(self):
			with self.client:
				headers = {
	    		'Authorization': 'Basic ' + b64encode("{0}:{1}".format(g.token, 'unused'))
				}
				response = self.client.get('/api/v1.0/main/menu', headers=headers)
				print 'test result is ' + str(response.data)
				self.assertEqual(response.status_code, 200)


	def setUp(self):
		print '--------- setUp started ---------'
		with self.client:
			username = 'mhb8432@gmail.com' # input your email in user table
			password = 'a123456' # input your password in user table
			headers = {
    		'Authorization': 'Basic ' + b64encode("{0}:{1}".format(username, password))
			}
			response = self.client.get('/api/v1.0/users/token', headers=headers)
			g.token = str(response.json.get('token'))
			print 'getToken is ' + g.token
			self.assertEqual(response.status_code, 200)
		print '--------- setUp ended g is '+g.token+' ---------'


