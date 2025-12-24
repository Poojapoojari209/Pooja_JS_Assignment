function counter() {
  let count = 0; // variable in outer scope

  return function() { // inner function (closure)
    count++;
    console.log("Current count:", count);
  };
}

// Create a counter instance
const myCounter = counter();

myCounter(); 
myCounter(); 
myCounter(); 

const myCounter1 = counter();
myCounter1();