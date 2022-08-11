// Use the redis client to store a hash value, then retrieve all as object
import { createClient, print } from 'redis';
const client = createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

const updateCache = (key, value) => {
  client.hSet('cache', key, value, print);
}

const getCache = () => {
  client.hGetAll('cache', (err, obj) => {
    if (err) throw err;
    console.log(obj);
  });
}

updateCache('Portland', '50');
updateCache('Seattle', '80');
updateCache('New York', '20');
updateCache('Bogota', '20');
updateCache('Cali', '40');
updateCache('Paris', '2');
getCache();
