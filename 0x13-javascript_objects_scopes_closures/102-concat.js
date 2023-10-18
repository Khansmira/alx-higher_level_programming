#!/usr/bin/node

const files = require ('fs');

const pathA = process.argv[2];
const pathB = process.argv[3];
const pathC = process.argv[4];

function concatFiles (pathA, pathB, pathC) {
  files.readFile(pathA, 'utf8', (err, dataA) => {
    if (err) {
      console.error(err);
      return;
    }
    files.readFile(pathB, 'utf8', (err, dataB) => {
      if (err) {
        console.error(err);
        return;
      }

      const concatData = dataA + dataB;

      files.writeFile(pathC, concatData, 'utf8', (err) => {
        if (err) {
	  console.error(err);
	}
      });
    });
  });
    concatFiles(pathA, pathB, pathC);
