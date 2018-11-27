// Node 11.2.0

fs = require('fs');


const input = fs.readFileSync('input.txt', 'utf-8').split('\n');


function validTriangle(a, b, c) {
  return a + b > c && b + c > a && c + a > b;
}


let count = 0;

for (let tri of input) {
  let m = tri.match(/(.{5})(.{5})(.{5})/);
  let a = parseInt(m[1]);
  let b = parseInt(m[2]);
  let c = parseInt(m[3]);

  if (validTriangle(a, b, c))
    count++;
}

console.log(count);
