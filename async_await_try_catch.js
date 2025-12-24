// A function that returns a Promise, simulating an async operation
function fetchData(shouldSucceed) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (shouldSucceed) {
        resolve("Data fetched successfully!");
      } else {
        reject(new Error("Failed to fetch data."));
      }
    }, 1000); // Simulate network delay
  });
}

// An async function using try...catch
async function getDataAndHandleErrors() {
  try {
    console.log("Attempting to fetch data...");
    const result = await fetchData(true); // Try with true for success
    console.log("Success:", result);

    console.log("\nAttempting to fetch data (with error)...");
    const errorResult = await fetchData(false); // Try with false for error
    console.log("This line will not be reached if an error occurs:", errorResult);
  } catch (error) {
    console.error("Error caught:", error.message);
  } finally {
    console.log("Operation attempt finished.");
  }
}

getDataAndHandleErrors();