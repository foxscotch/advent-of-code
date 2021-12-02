// Node 11.2.0

fs = require("fs");
crypto = require("crypto");

const input = "cxdnnyjw";

const start = process.hrtime.bigint();

let password = [null, null, null, null, null, null, null, null];
let i = 0;

while (true) {
  hash = crypto.createHash("MD5");
  hash.update(input + i++);
  let digest = hash.digest("hex");

  if (digest.startsWith("00000")) {
    let position = parseInt(digest[5]);
    let character = digest[6];

    if (isNaN(position) || position > 7 || password[position] !== null) {
      continue;
    } else {
      password[position] = character;
    }

    if (!password.includes(null)) {
      break;
    }
  }
}

console.log(password.join(""));

console.log(process.hrtime.bigint() - start);
