#!/usr/bin/node

const Square = require('./5-square.js'); {

class Square extends square {
  constructor(size) {
    super(size, size);
  }
   charPrint (c) {
     if (c === undefined) {
       this.print();
     } else { 
       for (let n = 0; n < this.height; n++) console.log(c.repeat(this.width));
     }
  }
};

module.exports = Square
