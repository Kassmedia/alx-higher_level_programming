#!/usr/bin/node

// Get the first argument (number of occurrences of element)
const x = parseInt(process.argv[2]);

// Check if the argument is a number
if (isNaN(x)) {
  // Print error message if not a number
  console.log('Missing number of occurrences');
} else {
  // Loop to print "C is fun" x times
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
