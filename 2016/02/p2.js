// Node 11.2.0

fs = require("fs");

const input = fs.readFileSync("input.txt", "utf-8").trim().split("\n");

// Just to make the array prettier
const A = "A";
const B = "B";
const C = "C";
const D = "D";
const _ = null;

class Keypad {
  constructor() {
    this.keypad = [
      [_, _, 1, _, _],
      [_, 2, 3, 4, _],
      [5, 6, 7, 8, 9],
      [_, A, B, C, _],
      [_, _, D, _, _],
    ];
    this.pos = { x: 0, y: 2 };
    this.pressed = [];
  }

  value(x, y) {
    if (typeof x === "undefined") x = this.pos.x;
    if (typeof y === "undefined") y = this.pos.y;

    return this.keypad[y][x];
  }

  press() {
    this.pressed.push(this.value());
  }

  move(dir) {
    if (dir === "U") this.up();
    else if (dir === "D") this.down();
    else if (dir === "L") this.left();
    else this.right();
  }

  up() {
    if (this.pos.y > 0 && this.value(undefined, this.pos.y - 1) !== null)
      this.pos.y--;
  }

  down() {
    if (this.pos.y < 4 && this.value(undefined, this.pos.y + 1) !== null)
      this.pos.y++;
  }

  left() {
    if (this.pos.x > 0 && this.value(this.pos.x - 1) !== null) this.pos.x--;
  }

  right() {
    if (this.pos.x < 4 && this.value(this.pos.x + 1) !== null) this.pos.x++;
  }

  result() {
    return this.pressed.join("");
  }
}

k = new Keypad();
for (let key of input) {
  for (let dir of key) {
    k.move(dir);
  }
  k.press();
}
console.log(k.result());
