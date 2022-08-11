const kue = require('kue'),
  queue = kue.createQueue();


const blacklisted = ['4153518780', '4153518781'];


const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  //check if phone number is blacklisted
  if (blacklisted.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

  // Create a queue job to send a notification to a phone number

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
