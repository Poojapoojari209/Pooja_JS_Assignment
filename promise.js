//simple promise pogram

let promise = new Promise((resolve, reject) => {
    let success = true;

    if(success){
        resolve("Task completed succssfully");

    }else{
        reject("Task failed");
    }
});

promise
.then((msg) => console.log(msg))
.catch((err) => console.log(err))



// Promise method - Promise.all
let p1 = Promise.resolve("first done");
let p2 = Promise.resolve("second done");
let p3 = Promise.resolve("Third done");

Promise.all([p1, p2, p3]).then((values) => {
    console.log(values);
});


// Promise method - Promise.race
let Pro1 = new Promise((resolve) => setTimeout(() => resolve("one"), 2000));
let pro2 = new Promise((resolve) => setTimeout(() => resolve("Two"), 3000));

Promise.race([Pro1, pro2]).then((results) => console.log(results));