#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const nameFile = process.argv[3];
let text;

request(url, errorFunc);

function errorFunc (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    text = body;
    fs.writeFile(nameFile, text, 'utf-8', errorFunc2);

    function errorFunc2 (err) {
      if (err) {
        console.log(err);
      }
    }
  }
}
