// Node 11.2.0

fs = require('fs');


const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\n');


class Keypad {
  constructor() {
    this.keypad = [[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]];
    this.pos = { x: 1, y: 1 };
    this.pressed = [];
  }

  value() {
    return this.keypad[this.pos.y][this.pos.x];
  }

  press() {
    this.pressed.push(this.value());
  }

  move(dir) {
    if (dir === 'U')
      this.up();
    else if (dir === 'D')
      this.down();
    else if (dir === 'L')
      this.left();
    else
      this.right();
  }

  up() {
    if (this.pos.y > 0)
      this.pos.y--;
  }

  down() {
    if (this.pos.y < 2)
      this.pos.y++;
  }

  left() {
    if (this.pos.x > 0)
      this.pos.x--;
  }

  right() {
    if (this.pos.x < 2)
      this.pos.x++;
  }

  result() {
    return parseInt(this.pressed.join(''));
  }
}


k = new Keypad();
for (let key of input) {
  for (let dir of key) {
    k.move(dir);
  }
  k.press();
  console.log(k.value());
}
console.log(k.result());
