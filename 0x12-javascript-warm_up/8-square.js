#!/usr/bin/node

// Get the first argument (size of the square)
const size = parseInt(process.argv[2]);

// Check if the argument is a number
if (isNaN(size)) {
  // Print error message if not a number
  console.log('Missing size');
} else {
  // Nested loops to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row); // Print each row of X's
  }
}
