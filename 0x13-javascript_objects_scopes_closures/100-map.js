#!/usr/bin/node
const listImport = require('./100-data.js').list;

const listMultiplyIndex = [];
listImport.map((number, i) => {
  listMultiplyIndex.push(number * i);
  return listMultiplyIndex;
});

console.log(listImport);
console.log(listMultiplyIndex);
