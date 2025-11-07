//Common js modules

const myModule = require('./Common_JS_export'); 

const message = myModule.greet('World');
console.log(message); 

console.log(`The value of PI is: ${myModule.PI}`); 
