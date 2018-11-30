// Node 11.2.0

fs = require('fs');
crypto = require('crypto');


const input = 'cxdnnyjw';

const start = process.hrtime.bigint();


let password = '';
let i = 0;

while (true) {
  hash = crypto.createHash('MD5');
  hash.update(input + i);
  let digest = hash.digest('hex');
  if (digest.startsWith('00000')) {
    password += digest[5];
    if (password.length >= 8)
      break;
  }
  i++;
}

console.log(password);


console.log(process.hrtime.bigint() - start);
