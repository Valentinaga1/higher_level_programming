#!/usr/bin/node
let datos = 0;
if (process.argv.length <= 3) {
  console.log(datos);
} else {
  datos = process.argv.slice(2);
  datos.sort(function (a, b) { return b - a; });
  console.log(datos[1]);
}
/* if ((process.argv.length === 2) || (process.argv.length === 3)) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
    arr.sort();
  }
  console.log(arr[arr.length - 2]);
} */
