angular.module("MyApp", [])
    .controller("MyController", function () {
        this.patterns = {
            mail: {
                regex: /^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/,
                message: 'メールアドレス形式が不正です。'
            }
        };
    });