const { expect } = require('chai');
const request = require('request');

describe('API Test', () => {
  it('Tests that GET returns correct code and results', (done) => {
    request('http://localhost:7865/', (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Tests /cart/:id is working', (done) => {
    request('http://localhost:7865/cart/1', (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  });

  it('Tests /cart/:id fails when given non-number', (done) => {
    request('http://localhost:7865/cart/a', (_error, response, _body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
