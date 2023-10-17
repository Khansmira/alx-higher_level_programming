#!/usr/bin/node
const cArgs = process.argv.length;
console.log(cArgs === 2 ? 'No argument' : cArgs === 3 ? 'Argument found' : 'Arguments found');
