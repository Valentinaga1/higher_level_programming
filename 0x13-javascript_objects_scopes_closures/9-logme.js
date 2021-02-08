#!/usr/bin/node
let argumentPrinted = 0;
exports.logMe = function (item) {
  console.log(argumentPrinted + ': ' + item);
  argumentPrinted += 1;
};
