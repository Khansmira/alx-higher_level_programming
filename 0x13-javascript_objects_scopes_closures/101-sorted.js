#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

for (const key in dict) {
  const key = dict[key];

  if (!newDict[key]) {
  newDict[key] = [];
  }

  newDict[key].push(key);
}
  console.log(newDict);
