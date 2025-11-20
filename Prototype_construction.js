// 1. Define a constructor function
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// 2. Add methods and properties to the prototype
// These will be shared by all instances created with the Person constructor
Person.prototype.greet = function() {
  console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
};

Person.prototype.species = "Homo Sapiens";

// 3. Create instances of the Person object
const person1 = new Person("Alice", 30);
const person2 = new Person("Bob", 25);

// 4. Access properties and call methods
console.log(person1.name); // Output: Alice
person1.greet(); // Output: Hello, my name is Alice and I am 30 years old.
console.log(person1.species); // Output: Homo Sapiens

console.log(person2.name); // Output: Bob
person2.greet(); // Output: Hello, my name is Bob and I am 25 years old.
console.log(person2.species); // Output: Homo Sapiens

// 5. Demonstrate prototype chain
console.log(person1.__proto__ === Person.prototype); // Output: true
console.log(Person.prototype.__proto__ === Object.prototype); // Output: true