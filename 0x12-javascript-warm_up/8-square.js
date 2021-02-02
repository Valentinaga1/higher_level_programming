#!/usr/bin/node
const x = '';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    x = "";
    for (let j = 0; j < process.argv[2]; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
