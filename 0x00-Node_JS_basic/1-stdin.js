// display the message Welcome to Holberton School,
// what is your name?
// user should be able to input their name on a new lin
// display the message Hello <name>, nice to meet you!

console.log('Welcome to Holberton School, what is your name?');

process.stdin
  .on('readable', () => {
    const input = process.stdin.read();
    if (input) {
      process.stdout.write(`Your name is: ${input}`);
    }
  })

  .on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
