(function() {
  'use strict';

  angular
    .module('articleManager')
    .run(runBlock);

  /** @ngInject */
  function runBlock($log) {

    $log.debug('runBlock end');
  }

})();
