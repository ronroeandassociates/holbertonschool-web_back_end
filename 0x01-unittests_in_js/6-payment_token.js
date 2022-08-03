function getPaymentTokenFromAPI(success) {
  if (success === true) {
    return new Promise((resolve, _reject) => {
      const object = {
        data: 'Successful response from the API',
      };
      resolve(object);
    });
  }
}

module.exports = getPaymentTokenFromAPI;
