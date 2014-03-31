  angular.module('App.Services', [])
  
  .config(['$httpProvider', function ($httpProvider) {
  	console.log('---- .config(function($httpProvider){ ---- ');
    $httpProvider.interceptors.push('$authInterceptor');
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
  }])	
	
  .factory('$authInterceptor', ['$q', '$window', '$location', '$Base64',function($q, $window, $location, $Base64){
  	return {

  		request: function(config){
  			config.headers = config.headers || {}
  			if($window.sessionStorage.token){
  				console.log('### config.url ' + config.url + ':'+config.url.indexOf('token'));
  				if(config.url.indexOf('token') == -1){
  					config.headers.Authorization = 'Basic ' + $Base64.encode($window.sessionStorage.token+':unused');
  					console.log('$authInterceptor header:');
  					console.log(config.headers);
  				}
  			}
  			return config || $q.when(config);
  		},

  		response: function(response){
  			return response || $q.when(response);
  		},

  		requestError: function(rejection){
  			return $q.reject(rejection);
  		},

  		responseError: function(rejection){
  			if(rejection.status == 401){
  				$window.sessionStorage.token = '';
  				console.log('rejection.url' + rejection.config.url);
  				$location.path('/login')
  			}
        return $q.reject(rejection);
  		}
  	};
  }])

  .factory('$appUser', ['$q', '$http', '$window', '$Base64', 
  		function($q, $http, $window, $Base64){
		var callbackToken = 'JSON_CALLBACK';
		var authenticateUrl = 'http://localhost:5001/api/v1.0/users/token'; 
		var keyPrefix = 'user-';
		var userIdentifyKey = keyPrefix + 'user'
		return {
			prefixKey : function(value) {
				return keyPrefix + value;
			},

			login: function(email, password){
				
				var user = {email: email, password:password};
				var url = authenticateUrl;
				$http.defaults.headers.common['Authorization'] = 'Basic ' + $Base64.encode(email+':'+password);
    		var headers = {'Authorization' : 'Basic ' + $Base64.encode(email+':'+password)};
    		var deferred = $q.defer();

				$http({method:'GET', url:url, headers:headers, withCredentials: true})
						.success(function(data, status, headers, config){
							$window.sessionStorage.token = data.token;
							$window.sessionStorage.user = JSON.stringify(user);
							deferred.resolve(user);
						})
						.error(function(data, status, headers, config){
							console.log("login error = [" + status + ":" +data + "]");
							deferred.resolve({email:'',password:''});
						})
					return deferred.promise;
			},

			isLogined: function(){
				console.log($window.sessionStorage.user);
				if($window.sessionStorage.user){
					return {
						value: true,
						user : JSON.parse($window.sessionStorage.user)
					};
				}else
					return {
						value:false,
						user:{}
					};
			},

			logout: function(){
				$window.sessionStorage.user = '';
				$window.sessionStorage.token = '';
				return true;
			}
		};
  }])

  .factory('$appMenus', ['$q', '$http', '$window', function($q, $http, $window){
  	var searchToken = []
  	var appMenusUrl = 'http://localhost:5001/api/v1.0/main/menu';
  	var keyPrefix = 'menus-'
  	return {

  		prefixKey : function(value) {
				return keyPrefix + value;
			},

			query: function(q, cache, onSuccess, onFailure){

        onSuccess = onSuccess || function() {};
        onFailure = onFailure || function() {};

				var that = this;
				var key = that.prefixKey(q.join(','));
				var url = appMenusUrl;
				for(i=0;i<searchToken.length;i++){
					url += appMenusUrl.replace(searchToken[i], q[i]);
				}
        console.log('$appMenus query url is ' + url);
				$http({method:'GET', url:url})
					.success(function(data){
						onSuccess(q, data);
					})
					.error(function(data){
						onFailure(q);
					})
			},

			get: function(sqlid){
				var that = this;
				var deferred = $q.defer();
				that.query([], false, function(q, data){
					deferred.resolve(data);
				}, function(q){
					console.log(keyPrefix +  'error q is ' + q);
				});
				return deferred.promise;
			}

  	}

  }])

  .factory('$Base64', function() {
    var keyStr = 'ABCDEFGHIJKLMNOP' +
            'QRSTUVWXYZabcdef' +
            'ghijklmnopqrstuv' +
            'wxyz0123456789+/' +
            '=';
    return {
        encode: function (input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;

            do {
                chr1 = input.charCodeAt(i++);
                chr2 = input.charCodeAt(i++);
                chr3 = input.charCodeAt(i++);

                enc1 = chr1 >> 2;
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                enc4 = chr3 & 63;

                if (isNaN(chr2)) {
                    enc3 = enc4 = 64;
                } else if (isNaN(chr3)) {
                    enc4 = 64;
                }

                output = output +
                        keyStr.charAt(enc1) +
                        keyStr.charAt(enc2) +
                        keyStr.charAt(enc3) +
                        keyStr.charAt(enc4);
                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = "";
            } while (i < input.length);

            return output;
        },

        decode: function (input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;

            // remove all characters that are not A-Z, a-z, 0-9, +, /, or =
            var base64test = /[^A-Za-z0-9\+\/\=]/g;
            if (base64test.exec(input)) {
                alert("There were invalid base64 characters in the input text.\n" +
                        "Valid base64 characters are A-Z, a-z, 0-9, '+', '/',and '='\n" +
                        "Expect errors in decoding.");
            }
            input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

            do {
                enc1 = keyStr.indexOf(input.charAt(i++));
                enc2 = keyStr.indexOf(input.charAt(i++));
                enc3 = keyStr.indexOf(input.charAt(i++));
                enc4 = keyStr.indexOf(input.charAt(i++));

                chr1 = (enc1 << 2) | (enc2 >> 4);
                chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
                chr3 = ((enc3 & 3) << 6) | enc4;

                output = output + String.fromCharCode(chr1);

                if (enc3 != 64) {
                    output = output + String.fromCharCode(chr2);
                }
                if (enc4 != 64) {
                    output = output + String.fromCharCode(chr3);
                }

                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = "";

            } while (i < input.length);

            return output;
        }
    };
	})

  ;


