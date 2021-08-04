#!/usr/bin/node
exports.esrever = function (list) {
  let rever = [];
  for (let i = 0; i < list.length; i++) {
    rever.unshift(list[i]);
  }
  return rever;
};
