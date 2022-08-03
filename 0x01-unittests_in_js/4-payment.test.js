const sendPaymentRequestToAPI = require('./4-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');

describe('Test suite', () => {
  it('Test that sendPaymentRequestToAPI sums two rounded numbers', () => {
    const spy = sinon.stub(Utils, 'calculateNumber');
    sendPaymentRequestToAPI(1, 2);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 1, 2)).to.be.true;
    spy.restore();
  })
})
