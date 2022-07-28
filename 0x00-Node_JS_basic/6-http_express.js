// create a small HTTP server using Express module

const express = require('express');

const port = 1245;

const app = express();

app.get('/', (_req, res) => res.send('Hello Holberton School!'))
  .listen(port);

module.exports = app;
