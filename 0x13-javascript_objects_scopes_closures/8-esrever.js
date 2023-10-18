#!/usr/bin/node

exports.esrever = function (list) {
  if (list.length === 0) {
    return [];
  }
  const revList = [list[list.length - 1]];
  let c;
  for (c = list.length - 2; c > -1; c--) {
    revList.push(list[c]);
  }
  return revList;
};
