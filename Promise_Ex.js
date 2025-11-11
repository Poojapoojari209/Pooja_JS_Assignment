// Simulate an API call using Promise
function getUserData(userId) {
  return new Promise((resolve, reject) => {
    console.log("Fetching user data...");

    // Simulate network delay
    setTimeout(() => {
      const users = {
        1: { name: "Pooja", role: "Web Developer" },
        2: { name: "Arun", role: "Backend Developer" },
      };

      // Simulate success or failure
      if (users[userId]) {
        resolve(users[userId]); // success
      } else {
        reject("User not found"); // failure
      }
    }, 2000);
  });
}

// Use the Promise
getUserData(1)
  .then((user) => {
    console.log("✅ User fetched successfully:", user);
  })
  .catch((error) => {
    console.error(" Error:", error);
  })
  .finally(() => {
    console.log("Fetch operation completed.");
  });
