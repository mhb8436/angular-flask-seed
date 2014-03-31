angular.module('App.Routes', [])

  .config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    if(CONFIG.routing.html5Mode) {
      $locationProvider.html5Mode(true);
    }
    else {
      var routingPrefix = CONFIG.routing.prefix;
      if(routingPrefix && routingPrefix.length > 0) {
        $locationProvider.hashPrefix(routingPrefix);
      }
    }

    ROUTER.when('login_path', '/login', {
      controller : 'UserCtrl',
      templateUrl : CONFIG.prepareViewTemplateUrl('login')
    });

    ROUTER.when('home_path', '/home', {
      controller : 'HomeCtrl',
      templateUrl : CONFIG.prepareViewTemplateUrl('home')
    });

    ROUTER.otherwise({
      redirectTo : '/login'
    });

    ROUTER.install($routeProvider);
  }])
  .run(['$rootScope', '$location', function($rootScope, $location) {
    var prefix = '';
    if(!CONFIG.routing.html5Mode) {
      prefix = '#' + CONFIG.routing.prefix;
    }
    $rootScope.route = function(url, args) {
      return prefix + ROUTER.routePath(url, args);
    };

    $rootScope.r = $rootScope.route;

    $rootScope.c = function(route, value) {
      var url = ROUTER.routePath(route);
      if(url == $location.path()) {
        return value;
      }
    };
  }])
  ;
