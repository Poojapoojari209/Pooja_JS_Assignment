// //fetching the data 
// function fetchData(){
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             resolve("Data fetched successfully");
//         }, 2000);
//     });

// }

// //Async function await
// async function getData(){
//     console.log("fetching data");

//     const result = await fetchData();

//     console.log(result);
//     console.log("Process completed")
// }

// getData();

async function getMessage() {
    let promise = new Promise((resolve) => {
        setTimeout(() => resolve("Data received"), 2000);
    });

    let result = await promise;
    console.log(result);
}

getMessage();
