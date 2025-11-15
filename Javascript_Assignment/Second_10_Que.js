//1. Explain global scope, function scope, and block scope. 
    
var x = 10; // global variable

    function printX() {
    console.log(x); // accessible
    }

    printX();   
    console.log(x);


    function test() {
    var a = 20;   // function scoped
    console.log(a); 
    }

    test();       // 20
    console.log(a);


     if (true) {
    let b = 30;
    const c = 40;
    var d = 50;
    }

    console.log(d); 
    console.log(b); 
    console.log(c); 


//4. What is lexical scope? 

     function outer() {
    let msg = "Hello";

    function inner() {
        console.log(msg); // inner can access outer
    }

    inner();
    }

    outer();  // Hello

//5.How do closures work in JavaScript? 

function createCounter() {
    let count = 0; // 'count' is a variable in the outer function's scope

    return function() { // This is the inner function, forming the closure
        count++;
        console.log(count);
    };
    }

    const counter1 = createCounter(); // 'counter1' now holds the inner function
    const counter2 = createCounter(); // 'counter2' holds a *separate* inner function

    counter1(); // Output: 1
    counter1(); // Output: 2

    counter2(); // Output: 1 (starts a new count for counter2)
    counter1(); // Output: 3 (counter1 continues its own count)

//8. What are immediately invoked function expressions (IIFEs)?
var counter = (function() {
    var count = 0; // This variable is private to the IIFE
    return {
        increment: function() {
        count++;
        console.log(count);
        },
        getCount: function() {
        return count;
        }
    };
    })();

    // Calling the increment function from the returned object
    counter.increment(); // Output: 1
    counter.increment(); // Output: 2

    // Trying to access the private variable directly will fail
    console.log(counter.count); // Output: undefined



//pure function


    function add(a, b) {
    return a + b;
    }



//higher-order function

//Higher-order function that takes an array and an operation function
    function applyOperationToArray(arr, operation) {
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(operation(arr[i]));
    }
    return result;
    }

    // Example operation functions (can be passed to applyOperationToArray)
    function square(num) {
    return num * num;
    }

    function double(num) {
    return num * 2;
    }

    function addTen(num) {
    return num + 10;
    }

    const numbers = [1, 2, 3, 4, 5];

    // Using the higher-order function with different operations
    const squaredNumbers = applyOperationToArray(numbers, square);
    console.log("Squared numbers:", squaredNumbers); // Output: [1, 4, 9, 16, 25]

    const doubledNumbers = applyOperationToArray(numbers, double);
    console.log("Doubled numbers:", doubledNumbers); // Output: [2, 4, 6, 8, 10]

    const addedTenNumbers = applyOperationToArray(numbers, addTen);
    console.log("Numbers plus ten:", addedTenNumbers); // Output: [11, 12, 13, 14, 15]


    //map

    const n = [1, 2, 3, 4, 5];
    const square = n.map((num) => num * num);
    console.log(square);

    //filter

    const s = [1, 2, 3, 4, 5];
    const even = s.filter((num) => num % 2 === 0);
    console.log(even);

    //reduce

    const t = [1, 2, 3, 4, 5];
    const sum = t.reduce((acc, curr) => acc + curr, 0);
    console.log(sum);

    //find
     const u = [1, 2, 3, 4, 5];
    const fEven = u.find((num) => num % 2 === 0);
    console.log(fEven);