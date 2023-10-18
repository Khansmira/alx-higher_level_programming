#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    let printRow = '';
    let i = 0;
    while (i < this.width) {
      i++;
      printRow += 'X';
    }
     let j = 0;	  
     while (j < this.height) {
       j++;
       console.log(printRow);
     }
  }
}

module.exports = Rectangle;
