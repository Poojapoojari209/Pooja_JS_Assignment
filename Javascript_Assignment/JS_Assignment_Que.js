//3. What is the difference between var, let, and const?  
 // var example
    function varExample() {
    var x = 1;
    if (true) {
        var x = 10; // Reassigns the outer 'x'
        console.log("Inside block:", x); 
    }
    console.log("Outside block:", x); 
    }
    varExample();


    // let example
    function letExample() {
    let y = 2;
    if (true) {
        let y = 20; // Creates a new 'y' with block scope
        console.log("Inside block:", y); 
    }
    console.log("Outside block:", y); 
    }
    letExample();


    // const example
    function constExample() {
    const PI = 3.14;
    // PI = 3.14159; 
    console.log(PI);

    const MY_OBJECT = { value: 1 };
    // MY_OBJECT = { value: 2 }; // This would cause an error
    MY_OBJECT.value = 2; 
    console.log(MY_OBJECT.value); 
    }
    constExample();


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




    //1.What is a callback function?
    
    function processUserInput(name, callback) {
      // Simulate some processing or asynchronous task
      setTimeout(() => {
        const greetingMessage = `Hello, ${name}!`;
        callback(greetingMessage); // Execute the callback function with the result
      }, 1000); // Simulate a 1-second delay
    }
    
    function displayGreeting(message) {
      console.log(message);
    }
    
    // Call processUserInput and pass displayGreeting as the callback
    processUserInput("Alice", displayGreeting);
    // Expected output after 1 second: "Hello, Alice!"
    
    
    
    
    
    //2. What are arrow functions, and how are they different from normal functions?
    
    // Normal Function
    function add(a, b) {
      return a + b;
    }
    console.log(add(2, 3)); // Output: 5
    
    // Arrow Function (concise for single expression)
    const subtract = (a, b) => a - b;
    console.log(subtract(5, 2)); // Output: 3
    
    // Arrow Function with multiple statements (requires curly braces and return)
    const multiply = (a, b) => {
      let result = a * b;
      return result;
    };
    console.log(multiply(4, 5)); // Output: 20
    
    // 'this' binding example
    const person = {
      name: "Alice",
      normalMethod: function() {
        console.log("Normal method 'this.name':", this.name); // 'this' refers to 'person'
      },
      arrowMethod: () => {
        console.log("Arrow method 'this.name':", this.name); // 'this' refers to the global object (window/undefined in strict mode)
      }
    };
    
    person.normalMethod();
    person.arrowMethod();
    
    
    
    
    
    //3. What is the value of this inside an arrow function?
    
    // Global scope
    const globalObject = this; // In a browser, this would be the window object
    
    const arrowFunctionInGlobal = () => {
      console.log(this === globalObject); // true
    };
    
    arrowFunctionInGlobal(); // 'this' refers to the global object
    
    const myObject = {
      name: 'Example Object',
      regularMethod: function() {
        console.log(this.name); // 'this' refers to myObject
        const arrowFunctionInsideMethod = () => {
          console.log(this.name); // 'this' still refers to myObject (inherited from regularMethod's scope)
        };
        arrowFunctionInsideMethod();
      },
      arrowMethod: () => {
        console.log(this.name); // 'this' refers to the global object (inherited from the scope where myObject was defined)
      }
    };
    
    myObject.regularMethod();
    myObject.arrowMethod();
    
    
    
    
    
    //5 What is the difference between call, apply, and bind?
    
    const person1 = {
      firstName: "John",
      lastName: "Doe",
      getFullName: function(city, profession) {
        return `${this.firstName} ${this.lastName} from ${city} works as a ${profession}.`;
      }
    };
    
    const person2 = {
      firstName: "Jane",
      lastName: "Smith"
    };
    
    // --- Using call() ---
    // Executes immediately, arguments are passed individually.
    console.log(person.getFullName.call(person2, "New York", "Engineer"));
    // Output: Jane Smith from New York works as a Engineer.
    
    // --- Using apply() ---
    // Executes immediately, arguments are passed as an array.
    const args = ["London", "Doctor"];
    console.log(person.getFullName.apply(person2, args));
    // Output: Jane Smith from London works as a Doctor.
    
    // --- Using bind() ---
    // Does not execute immediately. Creates a new function.
    const boundGetFullName = person.getFullName.bind(person2, "Paris");
    // 'boundGetFullName' now has 'this' set to person2 and "Paris" is a pre-set argument.
    
    // Now we can call the new function later, and only need to pass the remaining arguments.
    console.log(boundGetFullName("Artist"));
    // Output: Jane Smith from Paris works as a Artist.
    
    
    
    
    
    //6. How do you pass parameters by reference vs value?
    
    //Pass by Value
    
    function modifyPrimitive(num) {
      num = num + 10; // Modifies the local copy of 'num'
      console.log("Inside function (primitive):", num);
    }
    
    let originalNumber = 5;
    console.log("Before function call (primitive):", originalNumber);
    modifyPrimitive(originalNumber);
    console.log("After function call (primitive):", originalNumber); // originalNumber remains 5
    
    
    //pass by reference
    function modifyObject(obj) {
      obj.property = "updated value"; // Modifies the original object's property
      console.log("Inside function (object):", obj);
    }
    
    let originalObject = { property: "original value" };
    console.log("Before function call (object):", originalObject);
    modifyObject(originalObject);
    console.log("After function call (object):", originalObject); // originalObject's property is updated
    
    
    
    
    //7.  What are default parameters in ES6?
    
    function greet(name = "Guest", greeting = "Hello") {
      console.log(`${greeting}, ${name}!`);
    }
    
    // Case 1: No arguments provided
    greet(); 
    // Output: Hello, Guest!
    
    // Case 2: Only 'name' argument provided
    greet("Alice"); 
    // Output: Hello, Alice!
    
    // Case 3: Both arguments provided
    greet("Bob", "Hi"); 
    // Output: Hi, Bob!
    
    // Case 4: 'undefined' explicitly passed for a parameter
    greet(undefined, "Greetings"); 
    // Output: Greetings, Guest! 
    // (name defaults to "Guest" because undefined was passed)
    
    greet("Charlie", undefined);
    // Output: Hello, Charlie!
    
    
    
    
    
    //9. What is the difference between function declaration and expression?
    
    //Function declartion
    function greet(name) {
      return `Hello, ${name}!`;
    }
    
    console.log(greet("Alice")); // Output: Hello, Alice!
    
    //function expression
    
    // Anonymous function expression
    const sayHello = function(name) {
      return `Hello, ${name}!`;
    };
    
    console.log(sayHello("Bob")); // Output: Hello, Bob!
    
    // Named function expression (name is local to the function's scope)
    const factorial = function calculateFactorial(n) {
      if (n <= 1) {
        return 1;
      }
      return n * calculateFactorial(n - 1);
    };
    
    console.log(factorial(5)); // Output: 120
    
    
    
    
    
    //10.What is a generator function?
    
    function* numberGenerator() {
      yield 1;
      yield 2;
      yield 3;
      return "Finished!"; // The return value is the final value when done is true
    }
    
    // Create a generator object
    const generator = numberGenerator();
    
    console.log(generator.next()); // Output: { value: 1, done: false }
    console.log(generator.next()); // Output: { value: 2, done: false }
    console.log(generator.next()); // Output: { value: 3, done: false }
    console.log(generator.next()); // Output: { value: 'Finished!', done: true }
    console.log(generator.next()); // Output: { value: undefined, done: true }