// Node 11.2.0

const fs = require("fs");

function getInput() {
  return fs.readFileSync("input.txt", "utf-8").trim().split("\n");
}

function main() {
  const puzzle = getInput();

  // Code here
}

if (module === require.main) {
  const start = process.hrtime.bigint();
  console.log(main());
  console.log(process.hrtime.bigint() - start);
}
