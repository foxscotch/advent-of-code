// Node 11.2.0

fs = require("fs");

const input = fs.readFileSync("input.txt", "utf-8").trim().split(", ");

class Walker {
  constructor(instructions) {
    this.x = 0;
    this.y = 0;
    this.direction = "n"; // n, s, e, or w
    this.instructions = instructions;
    this.visited = ["(0, 0)"];
  }

  walk() {
    for (let instr of this.instructions) {
      if (instr[0] == "L") this.left();
      else this.right();

      if (this.forward(parseInt(instr.slice(1)))) break;
    }

    return Math.abs(this.x) + Math.abs(this.y);
  }

  forward(steps) {
    for (let i = 0; i < steps; i++) {
      if (this.direction === "n") this.y++;
      else if (this.direction === "e") this.x++;
      else if (this.direction === "s") this.y--;
      else this.x--;

      let loc = `(${this.x}, ${this.y})`;
      if (this.visited.includes(loc)) return true;
      else this.visited.push(loc);
    }
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
