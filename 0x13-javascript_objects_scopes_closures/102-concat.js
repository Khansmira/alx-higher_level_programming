#!/usr/bin/node

const fs = require ('fs');

const pathA = fs.readFileSync(process.argv[2], 'utf8');
const pathB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], pathA + pathB);
