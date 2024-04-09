#!/usr/bin/node
/* a script that prints first arg converted to int */

const digit = process.argv[2];
if (isNaN(parseInt(digit))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${digit}`);
}
