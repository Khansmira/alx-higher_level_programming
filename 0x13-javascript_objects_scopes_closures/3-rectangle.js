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
    for(let i = 0; < this.width; i++) {
      printRow = printRow + 'X';
    }
    for (let j = 0; j < this.height; j++) {
       console.log(printRow);
     }
  }
}

module.exports = Rectangle;
