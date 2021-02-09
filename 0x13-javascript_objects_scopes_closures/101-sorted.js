#!/usr/bin/node
const dictImport = require('./101-data.js').dict;
const newDict = {};

for (const key in dictImport) {
  if (dictImport[key] in newDict) {
    newDict[dictImport[key]].push(key);
  } else {
    newDict[dictImport[key]] = [key];
  }
}
console.log(newDict);
