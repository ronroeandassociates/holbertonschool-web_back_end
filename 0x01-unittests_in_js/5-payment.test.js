const sendPaymentRequestToAPI = require('./5-payment');
const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');

describe('sendPaymentRequestToAPI', function() {
    let spy;
    beforeEach(() => {
      spy = sinon.spy(console, 'log');
    });
    afterEach(() => {
      spy.restore();
    });

  it('call sendPaymentRequestToAPI with 100, and 20', function() {
    sendPaymentRequestToAPI(100, 20);
    expect(spy.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
  it('call sendPaymentRequestToAPI with 10, and 10', function() {
    sendPaymentRequestToAPI(10, 10);
    expect(spy.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });
});
