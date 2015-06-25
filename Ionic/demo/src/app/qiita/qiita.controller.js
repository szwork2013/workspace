'use strict';

angular.module('mobileDemo')
  .controller('QiitaCtrl', function ($scope, $ionicLoading, $http) {

    var load = function(){
      // Loading... を表示
      $ionicLoading.show({
        template: 'Loading...'
      });

      // 本当は Factory 等に切り出した方がよさそうだが今回は省略
      $http.get('https://qiita.com/api/v1/items?per_page=30').success(function(items) {
        $scope.items = items;
        // Loading... を隠す
        $ionicLoading.hide();
      });
    };

    load();

    $scope.reload = function(){
      load();
    };

  });
