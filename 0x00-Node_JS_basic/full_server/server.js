// create a small Express server:

// It should use the routes defined in full_server/routes/index.js
// to serve the should use the port 1245

import express from 'express';

const routes = require('./routes/index');

const app = express();
const port = 1245;

app.use(routes);

app.listen(port);

export default app;
