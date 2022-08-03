const chai = require('chai');
const expect = chai.expect;
const request = require('request')

describe('API', function() {
  describe('GET /', function() {
    it('200, Welcome to the payment system', function(done) {
      const object = {
        url: 'http://127.0.0.1:7865',
        method: 'GET',
      };
      request(object, function(_error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
