// Node 9.3.0

const fork = require("child_process").fork;
const EventEmitter = require("events").EventEmitter;
const Queue = require("./Queue");

const divisor = 2147483647;
const last16 = 0b1111111111111111;

class Generator {
  constructor(startVal, factor, mult) {
    this.value = startVal;
    this.factor = factor;
    this.multipleOf = mult;
  }

  generate() {
    this.value = (this.value * this.factor) % divisor;
  }

  acceptable() {
    return this.value % this.multipleOf === 0;
  }

  static compare(a, b) {
    return (a & last16) === (b & last16);
  }
}

class Queues extends EventEmitter {
  constructor() {
    super();
    this.left = new Queue();
    this.right = new Queue();
  }

  queue(side, v) {
    this[side].enqueue(v);
    if (!this.left.isEmpty() && !this.right.isEmpty()) {
      this.emit("queued", this.left.dequeue(), this.right.dequeue());
    }
  }

  queueL(v) {
    this.queue("left", v);
  }
  queueR(v) {
    this.queue("right", v);
  }
}

function main() {
  const q = new Queues();
  const genA = new Generator(703, 16807, 4);
  const genB = new Generator(516, 48271, 8);

  const interval = setInterval(() => {
    if (genA.acceptable()) q.queueL(genA.value);
    if (genB.acceptable()) q.queueR(genB.value);

    genA.generate();
    genB.generate();
  });

  counter = 0;
  pairs = 0;
  q.on("queued", (a, b) => {
    pairs++;

    if (pairs % 100 == 0) console.log("queued", pairs);

    if (Generator.compare(a, b)) counter++;
    if (pairs >= 5000000) {
      genA.send({ type: "stop" });
      genB.send({ type: "stop" });
      console.log(counter);
    }
  });
}

if (require.main === module) main();
