// Create a function named countStudents. It should accept a path in argument
// The script should attempt to read the database file asynchronously
// The function should return a Promise
// If the database is not available, it should throw an error with the text Cannot load the database
// If the database is available, it should log the following message to the console
// Number of students: NUMBER_OF_STUDENTS
// It should log the number of students in each field, and the list with the following format:
// Number of students in FIELD:
// 6. List: LIST_OF_FIRSTNAMES
// CSV file can contain empty lines (at the end) - and they are not a valid student!

const fs = require('fs');

const countStudents = async (file) => {
  let content;
  try {
    content = await fs.promises.readFile(file, 'utf8');
  } catch (_error) {
    throw new Error('Cannot load the database');
  }

  let lines = content.split('\n');
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const field = lines.map((line) => line.split(',')[3]);
  const eachField = [...new Set(field)];

  const dict = {};

  for (let i = 0; i < eachField.length; i += 1) {
    const numStudents = field.filter(
      (fieldName) => fieldName === eachField[i],
    ).length;

    const studentsPerField = lines.filter(
      (line) => line.split(',')[3] === eachField[i],
    );

    const names = studentsPerField.map((line) => line.split(',')[0]);

    console.log(
      `Number of students in ${
        eachField[i]
      }: ${numStudents}. List: ${names.join(', ')}`,
    );

    dict[eachField[i]] = {
      numStudents,
      names,
    };
  }
  return dict;
};

module.exports = countStudents;
