// Upgrade the function you created in the previous task (0-calcul.js)
// Add a new argument named type at first argument of the function.


const calculateNumber = (type, a, b) => {
  if (type === 'SUM') return Math.round(a) + Math.round(b);
  if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
  if (type === 'DIVIDE'){
    if (Math.round(b) === 0) {
      return 'Error';
    } else {
      return Math.round(a) / Math.round(b);
    }
  }
};

module.exports = calculateNumber;
