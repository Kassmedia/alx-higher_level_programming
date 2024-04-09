#!/usr/bin/node
const a = process.argv.slice(2)[0];
if (a === undefined) {
  console.log('No argument');
} else {
  console.log(a);
}
