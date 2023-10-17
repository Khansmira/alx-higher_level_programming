#!/usr/bin/node
const a = process.argv[2];

if (!parseInt(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    let b = 0;
    let mySqr = '';

    while (b < a) {
      mySqr = mySqr + 'X';
      b++;
    }
    console.log(mySqr);
  }
}
