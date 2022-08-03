// Create a file 0-calcul.test.js that contains test cases of this function
// You can assume a and b are always number
// Tests should be around the “rounded” part

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe ('Test suite', () => {
  // Tests for calculateNumber function using Node.js assert
  it('Test that calculateNumber sums two rounded numbers', () => {
    expect(calculateNumber('SUM', 1, 2), 3);
    expect(calculateNumber('SUM', 1.1, 2.1), 3);
    expect(calculateNumber('SUM', 1.4, 2.4), 3);
    expect(calculateNumber('SUM', 1.9, 2.9), 5);
    expect(calculateNumber('SUM', 1.5, .5), 3);
    expect(calculateNumber('SUM', 2, 0), 2);
    expect(calculateNumber('SUM', -7, 2.1), -5);
    expect(calculateNumber('SUM', 8.4, -3), 5);
    expect(calculateNumber('SUM', -10.9, -3.6), -15);
    expect(calculateNumber('SUM', 0, 0), 0);
    expect(calculateNumber('SUM', -1, -1), -2);
    expect(calculateNumber('SUM', 0, -1), -1);
    expect(calculateNumber('SUM', -1, 0), -1);
    expect(calculateNumber('SUM', -8, 1), -7);
  });

  it('Test that calculateNumber subtracts two rounded numbers', () => {
    expect(calculateNumber('SUBTRACT', 1, 2), -1);
    expect(calculateNumber('SUBTRACT', 1.1, 2.1), -1);
    expect(calculateNumber('SUBTRACT', 1.4, 2.4), -1);
    expect(calculateNumber('SUBTRACT', 1.9, 2.9), -1);
    expect(calculateNumber('SUBTRACT', 1.5, .5), 1);
    expect(calculateNumber('SUBTRACT', 2, 0), 2);
    expect(calculateNumber('SUBTRACT', -7, 2.1), -9);
  });

  it('Test that calculateNumber divides two rounded numbers', () => {
    expect(calculateNumber('DIVIDE', -10.9, -3.6), 3);
    expect(calculateNumber('DIVIDE', 8, 4), 2);
    expect(calculateNumber('DIVIDE', 2.9, 1.4), 3);
    expect(calculateNumber('DIVIDE', -10, 2.3), -5);
    expect(calculateNumber('DIVIDE', -9, -2.9), 3);
    expect(calculateNumber('DIVIDE', 1.5, -3.8), -0.5);
    expect(calculateNumber('DIVIDE', 0, 0), 'Error');
    expect(calculateNumber('DIVIDE', -1, -1), 1);
    expect(calculateNumber('DIVIDE', 0, -1), 'Error');
    expect(calculateNumber('DIVIDE', -1, 0), 'Error');
    expect(calculateNumber('DIVIDE', -8, 1), -8);
  });
});
