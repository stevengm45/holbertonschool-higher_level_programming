#!/usr/bin/node
const args = process.argv;
const a = args[2];
const b = args[3];
function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    let sum = parseInt(a) + parseInt(b);
    return (sum);
  }
}
console.log(add(a, b));
