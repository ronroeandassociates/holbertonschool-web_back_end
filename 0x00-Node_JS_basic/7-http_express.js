// recreate the small HTTP server using Express
// HTTP server should listen on port 1245
// It should return plain text
// When the URL path is /, it should display Hello Holberton School!
// When the URL path is /students, it should display This is the list of our students
// followed by the same content as the file 3-read_file_async.js (with and without the database)
// the name of the database must be passed as argument of the file
// CSV file can contain empty lines (at the end) - and they are not a valid student!

const express = require('express');
const countStudents = require('./3-read_file_async.js');

const app = express();
const port = 1245;

app.get('/', (_req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (_req, res) => {
  res.write('This is the list of our students\n');
  await countStudents(process.argv[2])
    .then((data) => {
      const fields = Object.keys(data);
      const total = fields.reduce(
        (acc, curr) => acc + data[curr].NUMBER_OF_STUDENTS,
        0,
      );
      res.write(`Total number of students: ${total}\n`);
      for (let i = 0; i < fields.length; i += 1) {
        res.write(
          `${fields[i]}: ${data[fields[i]].NUMBER_OF_STUDENTS}\n`);
      }
      res.write('List of students:\n');
    })


      .catch((err) => {
        res.write(err.message);
      });
});

app.listen(port);

module.exports = app;
