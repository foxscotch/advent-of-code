// Node 11.2.0

const fs = require("fs");

function getInput() {
  return fs.readFileSync("input.txt", "utf-8").trim().split("\n");
}

function main() {
  const input = getInput();
  const positions = [];

  for (let i = 0; i < input[0].length; i++) {
    positions[i] = {};

    for (let msg of input) {
      const char = msg[i];
      if (typeof positions[i][char] === "undefined") positions[i][char] = 1;
      else positions[i][char]++;
    }
  }

  for (let ltrs of positions) {
    const ltr = Object.entries(ltrs).reduce((a, b) => (a[1] < b[1] ? a : b));
    process.stdout.write(ltr[0]);
  }

  console.log();
}

if (module === require.main) {
  const start = process.hrtime.bigint();
  main();
  console.log(process.hrtime.bigint() - start);
}
