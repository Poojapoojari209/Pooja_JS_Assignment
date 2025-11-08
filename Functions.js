// Traditional function expression
const addTraditional = function(p, q) {
  return p + q;
};

// Arrow function 
const addArrow = (a, b) => a + b;

console.log(addTraditional(5, 3)); 
console.log(addArrow(5, 3));  


// Anonymous Function Assigned to a Variable
const sayHello = function() {
  console.log("Hello from an anonymous function!");
};

sayHello(); 



//Anonymous Function as a Callback(with setTimeout)
setTimeout(function() {
  console.log("This message appears after 2 seconds.");
}, 2000);

//Anonymous Arrow Function
const multiply = (x, y) => x * y;

console.log(multiply(5, 3)); 



//immediate anonymous function
(function() {
  var message = "This is an immediate anonymous function!";
  console.log(message);
})();