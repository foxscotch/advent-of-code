// Node 11.2.0

fs = require("fs");

const input = fs.readFileSync("input.txt", "utf-8").split("\n");

function validTriangle({ a, b, c }) {
  return a + b > c && b + c > a && c + a > b;
}

const tris = [];

let tri1 = {};
let tri2 = {};
let tri3 = {};

let step = 0;
let count = 0;

for (let line of input) {
  step++;

  let m = line.match(/(.{5})(.{5})(.{5})/);
  let t1 = parseInt(m[1]);
  let t2 = parseInt(m[2]);
  let t3 = parseInt(m[3]);

  if (step % 3 === 1) {
    tri1.a = t1;
    tri2.a = t2;
    tri3.a = t3;
  } else if (step % 3 === 2) {
    tri1.b = t1;
    tri2.b = t2;
    tri3.b = t3;
  } else if (step % 3 === 0) {
    tri1.c = t1;
    tri2.c = t2;
    tri3.c = t3;

    tris.push(tri1, tri2, tri3);
    tri1 = {};
    tri2 = {};
    tri3 = {};
  }
}

for (let tri of tris) if (validTriangle(tri)) count++;

console.log(count);
