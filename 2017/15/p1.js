// Node 9.3.0

const divisor = 2147483647;
const last16 = 0b1111111111111111;


function generate(start, factor) {
  return (start * factor) % divisor;
}

function compare(genA, genB) {
  return (genA & last16) == (genB & last16);
}

function main() {
  let genA = 703;
  let genB = 516;
  const aFactor = 16807;
  const bFactor = 48271;

  counter = 0;
  for (let i = 0; i < 40000000; i++) {
    if (compare(genA, genB))
      counter++;
    genA = generate(genA, aFactor);
    genB = generate(genB, bFactor);
  }

  console.log(counter);
}


if (require.main == module) {
  main();
}
