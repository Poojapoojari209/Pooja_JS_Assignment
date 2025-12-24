console.log("Start of program");

// A function that returns a Promise
function simulateAsyncTask(message, delay) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(`Async task "${message}" completed after ${delay}ms`);
    }, delay);
  });
}

// An async function using await
async function performOperations() {
  console.log("Inside performOperations: Step 1");
  const result1 = await simulateAsyncTask("First operation", 1000);
  console.log(result1);

  console.log("Inside performOperations: Step 2");
  const result2 = await simulateAsyncTask("Second operation", 500);
  console.log(result2);

  return "All operations finished!";
}

// Call the async function and handle its returned Promise
performOperations().then((finalMessage) => {
  console.log(finalMessage);
});

console.log("End of program (synchronous part)");