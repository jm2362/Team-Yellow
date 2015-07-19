angular.module('app', ['ngRoute', 'ngTouch', 'ngResource', 'slick']);

angular.module('app')
    .config(function ($httpProvider) {
	$httpProvider.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
	$httpProvider.defaults.transformRequest = function(data){
	    if (data === undefined) {
		return data;
	    }
	    return $.param(data);
	}  
    })
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'partials/main.html',
                controller: 'MainController'
            })
           .when('/so-boxy', {
                templateUrl: 'partials/so-boxy.html',
            })
            .when('/banded', {
                templateUrl: 'partials/banded.html',
            })
            .when('/contact', {
                templateUrl: 'partials/contact.html',
            })
            .otherwise({redirectTo: '/'})
    });




