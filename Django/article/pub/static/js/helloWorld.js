//angular,djangoの競合回避
//http://qiita.com/giginet/items/7b5f3e0ce181c3345a55
(function(){
var myapp=anglular.module('myapp',[]);

myapp.config(function($interpolateProvider,$httpProvider){
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
	$httpProvider.defaults.xsrfCookieName='csrftoken'
	$httpProvider.defaults.xsrfHeaderName='X-CSRFToken'
});

//	.controller('HelloWorldController',function($scope){
//		$scope.message='Hello AngularJS World!';
//	});
myapp.controller('HelloWorldController',function($scope){
		$scope.message='Hello AngularJS World!';
});




var myApp=angular.module('myApp', []);
myApp.config(function($interpolateProvider){
	    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
	});
//function HelloWorldController($scope) {
//    $scope.message = 'Hello World!!';
//}
//(function(){
//	var myModule = angular.module('myapp',[]);
//	myModule.controller('HelloWorldController',function($scope){
//		$scope.message='Hello AngularJS World!';
//	});
//})();
})();
