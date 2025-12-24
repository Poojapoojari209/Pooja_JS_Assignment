//this in the Global Scope:
let globalVar = this;
console.log(globalVar === window); // true (in a browser)


//this Inside a Regular Function:
function showThis() {
  console.log(this === window); // true (in a browser)
}
showThis();

//this Inside an Object Method:
const person = {
  name: 'Alice',
  greet: function() {
    console.log(`Hello, my name is ${this.name}.`); // 'this' refers to 'person'
  }
};
person.greet(); // Output: Hello, my name is Alice.


//this Inside a Constructor
function Car(make, model) {
  this.make = make;
  this.model = model;
  this.display = function() {
    console.log(`This is a ${this.make} ${this.model}.`); // 'this' refers to the new Car instance
  };
}

const myCar = new Car('Toyota', 'Camry');
myCar.display(); // Output: This is a Toyota Camry.



// this Inside an Arrow Function:
const myObject = {
  value: 10,
  regularMethod: function() {
    console.log(this.value); // 'this' refers to myObject
  },
  arrowMethod: () => {
    console.log(this.value); // 'this' refers to the global object 
  }
};

myObject.regularMethod(); // Output: 10
myObject.arrowMethod(); // Output: undefined (or error if 'value' is not on global object)