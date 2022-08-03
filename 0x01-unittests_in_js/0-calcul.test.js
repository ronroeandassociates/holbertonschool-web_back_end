// Create a file 0-calcul.test.js that contains test cases of this function
// You can assume a and b are always number
// Tests should be around the “rounded” part

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe ('Test suite', () => {
  // Tests for calculateNumber function using Node.js assert
  it('Test that calculateNumber sums two rounded numbers', () => {
    assert.equal(calculateNumber(1, 2), 3);
    assert.equal(calculateNumber(1.1, 2.1), 3);
    assert.equal(calculateNumber(1.4, 2.4), 3);
    assert.equal(calculateNumber(1.9, 2.9), 5);
    assert.equal(calculateNumber(1.5, .5), 3);
    assert.equal(calculateNumber(2, 0), 2);
    assert.equal(calculateNumber(-7, 2.1), -5);
    assert.equal(calculateNumber(8.4, -3), 5);
    assert.equal(calculateNumber(-10.9, -3.6), -15);
    assert.equal(calculateNumber(0, 0), 0);
    assert.equal(calculateNumber(-1, -1), -2);
    assert.equal(calculateNumber(0, -1), -1);
    assert.equal(calculateNumber(-1, 0), -1);
    assert.equal(calculateNumber(-8, 1), -7);
  });
})
