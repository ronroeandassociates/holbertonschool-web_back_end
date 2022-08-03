// Create a file 0-calcul.test.js that contains test cases of this function
// You can assume a and b are always number
// Tests should be around the “rounded” part

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe ('Test suite', () => {
  // Tests for calculateNumber function using Node.js assert
  it('Test that calculateNumber sums two rounded numbers', () => {
    assert.equal(calculateNumber('SUM', 1, 2), 3);
    assert.equal(calculateNumber('SUM', 1.1, 2.1), 3);
    assert.equal(calculateNumber('SUM', 1.4, 2.4), 3);
    assert.equal(calculateNumber('SUM', 1.9, 2.9), 5);
    assert.equal(calculateNumber('SUM', 1.5, .5), 3);
    assert.equal(calculateNumber('SUM', 2, 0), 2);
    assert.equal(calculateNumber('SUM', -7, 2.1), -5);
    assert.equal(calculateNumber('SUM', 8.4, -3), 5);
    assert.equal(calculateNumber('SUM', -10.9, -3.6), -15);
    assert.equal(calculateNumber('SUM', 0, 0), 0);
    assert.equal(calculateNumber('SUM', -1, -1), -2);
    assert.equal(calculateNumber('SUM', 0, -1), -1);
    assert.equal(calculateNumber('SUM', -1, 0), -1);
    assert.equal(calculateNumber('SUM', -8, 1), -7);
  });
  it('Test that calculateNumber subtracts two rounded numbers', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 2), -1);
    assert.equal(calculateNumber('SUBTRACT', 1.1, 2.1), -1);
    assert.equal(calculateNumber('SUBTRACT', 1.4, 2.4), -1);
    assert.equal(calculateNumber('SUBTRACT', 1.9, 2.9), -1);
    assert.equal(calculateNumber('SUBTRACT', 1.5, .5), 1);
    assert.equal(calculateNumber('SUBTRACT', 2, 0), 2);
    assert.equal(calculateNumber('SUBTRACT', -7, 2.1), -9);
  });
  it('Test that calculateNumber divides two rounded numbers', () => {
    assert.equal(calculateNumber('DIVIDE', -10.9, -3.6), 3);
    assert.equal(calculateNumber('DIVIDE', 8, 4), 2);
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -1, -1), 1);
    assert.equal(calculateNumber('DIVIDE', 0, -1), 'Error');
    assert.equal(calculateNumber('DIVIDE', -1, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -8, 1), -8);
  })
})
