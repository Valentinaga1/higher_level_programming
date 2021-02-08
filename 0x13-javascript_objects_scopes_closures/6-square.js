#!/usr/bin/node
const SSquare = require('./5-square.js');

class Square extends SSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}
module.exports = Square;
