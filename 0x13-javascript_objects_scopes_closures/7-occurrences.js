#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      i++;
    }
  }
  return i;
};
