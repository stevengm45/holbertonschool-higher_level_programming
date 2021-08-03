#!/usr/bin/node
const secMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  secMax = args[args.length - 2];
}
console.log(secMax);

