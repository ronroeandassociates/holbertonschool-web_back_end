const Utils = require('./utils');

function sendPaymentRequestToAPI(totalAmount, totalShipping) {
  console.log(`The total is: ${Utils.calculateNumber('SUM', totalAmount, totalShipping)}`);
}

module.exports = sendPaymentRequestToAPI;
