#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (let x in list) {
    if (list[x] === searchElement) {
      i++;
    }
  }
  return i;
};
