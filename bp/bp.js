// Node 11.2.0

fs = require('fs');


const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');

const start = process.hrtime.bigint();


// Code here


console.log(process.hrtime.bigint() - start);
