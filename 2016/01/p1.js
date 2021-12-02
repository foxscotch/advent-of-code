// Node 11.2.0

fs = require("fs");

const input = fs.readFileSync("input.txt", "utf-8").trim().split(", ");

class Walker {
  constructor(instructions) {
    this.x = 0;
    this.y = 0;
    this.direction = "n"; // n, s, e, or w
    this.instructions = instructions;
  }

  walk() {
    for (let instr of this.instructions) {
      if (instr[0] == "L") this.left();
      else this.right();

      this.forward(parseInt(instr.slice(1)));
    }

    return Math.abs(this.x) + Math.abs(this.y);
  }

  forward(steps) {
    if (this.direction === "n") this.x += steps;
    else if (this.direction === "e") this.y += steps;
    else if (this.direction === "s") this.x -= steps;
    // this.direction == 'w'
    else this.y -= steps;
  }

  left() {
    if (this.direction === "n") this.direction = "w";
    else if (this.direction === "w") this.direction = "s";
    else if (this.direction === "s") this.direction = "e";
    else this.direction = "n";
  }

  right() {
    if (this.direction === "n") this.direction = "e";
    else if (this.direction === "e") this.direction = "s";
    else if (this.direction === "s") this.direction = "w";
    else this.direction = "n";
  }
}

w = new Walker(input);
console.log(w.walk());
