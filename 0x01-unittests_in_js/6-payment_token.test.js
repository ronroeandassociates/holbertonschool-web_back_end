
const chai = require('chai');
const expect = chai.expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe.only('getPaymentTokenFromAP', function() {
  const object = {
    data: 'Successful response from the API',
  };
  it('Async tests with done', function(done) {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.eql(object);
        done();
      }).catch((error) => {
        done(error);
      });
  });
});
