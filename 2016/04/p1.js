// Node 11.2.0

fs = require('fs');


const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');

const start = process.hrtime.bigint();


for (let room of input) {
  let [_, name, id, checksum] = room.match(/([\w-]+)-(\d{3})\[(\w+)\]/);
  name = name.replace(/-/g, '');
}


console.log(process.hrtime.bigint() - start);
