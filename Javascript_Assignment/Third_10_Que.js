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