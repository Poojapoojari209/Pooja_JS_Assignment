    const fs = require('fs');

    // --- Writing to a file (asynchronous) ---
    const contentToWrite = "Hello, Node.js File System!";
    fs.writeFile('output.txt', contentToWrite, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return;
        }
        console.log('Content written to output.txt successfully.');

        // --- Reading from a file (asynchronous) ---
        fs.readFile('output.txt', 'utf8', (err, data) => {
            if (err) {
                console.error('Error reading file:', err);
                return;
            }
            console.log('Content read from output.txt:', data);
        });
    });

    // --- Synchronous file writing ---
    try {
        fs.writeFileSync('sync_output.txt', 'This is synchronous content.');
        console.log('Synchronous content written to sync_output.txt.');
    } catch (err) {
        console.error('Error writing synchronously:', err);
    }