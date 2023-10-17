#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  Array.from({ length: x }, () => theFunction());
};
