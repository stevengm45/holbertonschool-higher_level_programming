#!/usr/bin/node
const args = process.argv;
const a = args[2];
const b = args[3];
function add(a, b) {
  return (parseInt(a) + parseInt(b));
  }
console.log(add(a, b));
