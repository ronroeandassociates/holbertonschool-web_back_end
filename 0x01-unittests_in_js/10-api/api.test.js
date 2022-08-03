const {expect} = require('chai');
const request = require("request");


describe('test - GET /api', () => {
  it('Tests GET returns correct code and res', (done) => {
    request('http://localhost:7865', (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('test - GET /api/cart/:id([0-9]*)', () => {
  it('Tests if /cart/:id([0-9]*) is working', (done) => {
    request('http://localhost:7865/cart/1', (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  });

  it('Tests /cart/:id fails when NaN', (done) => {
    request('http://localhost:7865/cart/a', (_error, response, _body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  })
});

describe('test - GET /api/available_payments', () => {
  it('Tests if /available_payments is working', (done) => {
    request('http://localhost:7865/available_payments', (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
      done();
    });
  });
});

describe('test - POST /api/login', () => {
  it('Tests if /login is working', (done) => {
    request({
      method: 'POST',
      uri: 'http://localhost:7865/login',
      json: {
        userName: 'Betty',
      }
    }, (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
