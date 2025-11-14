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


 