angular.module('App.Controllers',[])

	.controller('AppCtrl', ['$location', '$scope', function($location, $scope) {
		$scope.current_path = '#' + $location.url();
  }])

	.controller('UserCtrl', ['$location', '$scope','$routeParams','$appUser', '$Base64',
		function($location, $scope, $routeParams, $user, $Base64){
			console.log('UserCtrl started....');

			$scope.email = 'mhb8432@gmail.com';
			$scope.password = 'a123456';

			var prevurl = $routeParams.prevurl;
			prevurl = '/home'
			console.log(prevurl);
			$scope.user = $user.isLogined().user;

			$scope.submit = function(){
				if($scope.email && $scope.password){
					var promise = $user.login($scope.email, $scope.password);
					promise.then(function(data){
						$scope.user = data;
						if($scope.user){
							$location.path(prevurl);
						}
					});
				}				
			};

			$scope.logout = function(){
				if($user.logout()){
					$location.path('/login');
				}
			};
	}])

	.controller('HomeCtrl', ['$window','$timeout', '$location','$scope','$routeParams', '$filter', '$appMenus', '$appUser', 
		function($window, $timeout, $location, $scope, $routeParams, $filter, $menu, $user){
		$scope.menus = [];

		$scope.logout = function(){
			if($user.logout()){
				$location.path('/login');
			}
		};

		$scope.printMenus = function(){
			console.log('$scope.printMenus')
			var promise = $menu.get();
			promise.then(function(data){
				// console.log(data);
				$scope.menus = data || [];
				console.log('------$scope.menus------')
				console.log($scope.menus)
			});
		}

		$scope.printMenus();

	}])
	

	;