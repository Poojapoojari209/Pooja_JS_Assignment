//main.js  ES6 modules

import {add, subtraction} from './mathOperation.js';
import multiply from './mathOperation.js';

console.log("Addition", add(5, 3));
console.log("Subtract", subtraction(10, 4));
// console.log("PI value:", PI);
console.log("Multiplication:", multiply(7, 2));


//mainex.js  Common js modules

// const myModule = require('./mathOperation.js'); 

// const message = myModule.greet('World');
// console.log(message); 

// console.log(`The value of PI is: ${myModule.PI}`); 




//mainex.js AMD Module
    //  require(['mathOperation'], function(mathOperation) {
    //     console.log(mathOperation.getMessage());
    // });
   