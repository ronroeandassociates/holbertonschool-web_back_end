// module named utils.js

const Utils = {
  calculateNumber(type, a, b) {
    // Calculate rounded numbers based on type of function
      if (type === "SUM") {
        return Math.round(a) + Math.round(b);
      } else if (type === "SUBTRACT") {
        return Math.round(a) - Math.round(b);
      } else if (type === "DIVIDE") {
        if (Math.round(b) === 0) {
          return "Error";
        }
        return Math.round(a) / Math.round(b);
      } else {
        return "Error";
      }
    },
  };

  module.exports = Utils;
