#!/usr/bin/node

const { dict } = require('./101-data')

const newDict = {};

for (const userId in dict) {
  const key = dict[userId];

  if (!newDict[key]) {
  newDict[key] = [];
  }

  newDict[key].push(userId);
}
  console.log(newDict);
