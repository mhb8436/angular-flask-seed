'use strict';

/**
* Wave Frontend app module
* @type {angular.Module}
*/
console.log('------------------------------------------');
console.log('app.js');

var App = window.App = angular.module('App', 
	[
			'ngRoute',
	    'App.Controllers',
	    'App.Services',
	    'App.Directives',
	    'App.Routes'
	])
;