#!/usr/bin/node
let secMax = 0;
let args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  secMax = args[args.length - 2];
}
console.log(secMax);
