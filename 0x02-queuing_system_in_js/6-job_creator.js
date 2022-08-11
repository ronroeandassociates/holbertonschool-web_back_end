
// create a queue Kue with a name of "push_notification_code"
const kue = require('kue')
  , queue = kue.createQueue();

const jobData = {
  phoneNumber: 'string',
  message: 'string',
};

// create a job with a name of "push _notification_code"

const job = queue.create('push_notification_code', jobData).save(function (err) {
  if (!err) console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', function () {
    console.log('Notification job completed');
  })
  .on('failed attempt', function (_errorMessage, _doneAttempts) {
    console.log('Notification job failed');
});
