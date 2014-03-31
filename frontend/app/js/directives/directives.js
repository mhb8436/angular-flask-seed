angular.module('App.Directives', [])
	

	.directive('myMenu', ['$location', function($location){
		return {
			 restrict:'E'
			,replace: true
			,templateUrl: CONFIG.preparePartialTemplateUrl('menus')
			, link: function(scope, elem, attrs){
				console.log('--- directives scope.menus ----');
				console.log(scope.menus);
			}
		};
	}])
	;

	