console.log("Start");

setTimeout(() => {
  console.log("Timeout executed");
}, 0);

console.log("End");


console.log("1");

setTimeout(() =>
{
    console.log("2");
}, 1000);

console.log("3");

setTimeout(() =>
{
    console.log("4");
}, 0);

console.log("5");



//Microtask Queue Example (Promises)
//Microtasks run before setTimeout.

console.log("A");

setTimeout(() => console.log("B"), 0);

Promise.resolve().then(() => console.log("C"));

console.log("D");



console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");


async function demo(){
   
    console.log("1");

    setTimeout(() => console.log("2"), 0);

    await Promise.resolve();
    console.log("3");
    
    console.log("4");
}

demo()
console.log("5")


// //Promise real life example

function orderPizza() {
  return new Promise((resolve, reject) => {
    let isAvailable = true;

    console.log("Pizza order placed...");

    setTimeout(() => {
      if (isAvailable) {
        resolve("Pizza delivered!");
      } else {
        reject(" Pizza not available!");
      }
    }, 2000);
  });
}

orderPizza()
  .then((res) => console.log(res))
  .catch((err) => console.log(err));


 let swiggyOrder = new Promise((resolve, reject) => {
 
    setTimeout (() => {

        
    let sucess = true
   
   if(sucess)
   {
     resolve("accepted order")

   }
   else{
    reject("Out of stock")
   }

    }, 1000)
 
  });

  swiggyOrder.then((res) => console.log(res))
  .then(() => console.log("your order will reached shortly"))
  .catch((res) => console.log(res))
  .finally(() => console.log("Transaction completed"))

//   console.log("done")



//Promise all method
let p1 = Promise.resolve(10)
let p2 = new Promise((res, rej) => {
    res(20)
})

let p3 = new Promise((res, rej) => {
    setTimeout(() => { res(20)}, 2000)
})

Promise.all([p1, p2, p3]).then((result) => console.log)