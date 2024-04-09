#!/usr/bin/node
// prints script that searches the second biggest integer in the list of argument
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const check = process.argv.sort();
  console.log(check.reverse()[1]);
}
