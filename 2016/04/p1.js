// Node 11.2.0

fs = require('fs');


const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');


function getChecksum(name) {
  let ltrObj = {};

  for (let char of name.replace(/-/g, '')) {
    if (typeof ltrObj[char] === 'undefined')
      ltrObj[char] = 1;
    else
      ltrObj[char]++;
  }

  let ltrList = [];

  for (let [ltr, qty] of Object.entries(ltrObj)) {
    ltrList.push({ ltr, qty });
  }

  return ltrList.sort((a, b) => {
    if (a.qty === b.qty) {
      if (a.ltr > b.ltr)
        return 1;
      else if (a.ltr < b.ltr)
        return -1;
    } else {
      return b.qty - a.qty;
    }
  }).map(e => e.ltr).join('').slice(0, 5);
}


count = 0;

for (let room of input) {
  let [_, name, id, checksum] = room.match(/([\w-]+)-(\d{3})\[(\w+)\]/);
  if (checksum === getChecksum(name))
    count++;
}

console.log(count);
