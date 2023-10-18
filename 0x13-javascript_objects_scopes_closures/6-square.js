#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor(size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      let printRow = '';
      let i = 0;
      let j = 0;
      for (; i < this.width; i++) {
        printRow = printRow + c;	    
      for (; j < this.height; j++) {
        console.log(printRow);
      }
    }
  }
}

module.exports = Square
