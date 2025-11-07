 //AMD Modules
 define([], function() {
        function getMessage() {
            return "Hello from my AMD module!";
        }

        return {
            getMessage: getMessage
        };
    });
    