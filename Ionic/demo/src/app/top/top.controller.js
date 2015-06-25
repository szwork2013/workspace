'use strict';

angular.module('mobileDemo')
  .controller('TopCtrl', function ($scope, $ionicModal, $ionicPopover, $ionicActionSheet, $timeout) {

    // モーダル
    $ionicModal.fromTemplateUrl("top.modal.html", {
      scope: $scope,
      animation: "slide-in-up"
    }).then(function(modal) {
      $scope.modal = modal;
    });
    $scope.openTutorialModal = function() {
      $scope.modal.show();
    };
    $scope.closeTutorialModal = function() {
      $scope.modal.hide();
    };
    $scope.$on("$destroy", function() {
      $scope.modal.remove();
    });

    // ポップオーバー
    $ionicPopover.fromTemplateUrl("top.popover.html", {
      scope: $scope
    }).then(function(popover) {
      $scope.popover = popover;
    });
    $scope.openInfoPopover = function($event) {
      $scope.popover.show($event);
    };
    $scope.closeInfoPopover = function() {
      $scope.popover.hide();
    };
    $scope.$on("$destroy", function() {
      $scope.popover.remove();
    });

    // アクションシート(シェアボタン)
    $scope.share = function() {
      var hideSheet = $ionicActionSheet.show({
        buttons: [
          {
            text: "<font color='#4298ED'><i class='ion-social-twitter'></i></font>"
          }, {
            text: "<font color='red'><i class='ion-social-googleplus'></i></font>"
          }, {
            text: "<font color='#344A8D'><i class='ion-social-facebook'></i></font>"
          }
        ],
        titleText: "これはダミーです <i class='ion-sad-outline'></i>",
        buttonClicked: function(index) {}
      });
      $timeout((function() {
        hideSheet();
      }), 1500);
    };
  });
