// import redis
const redis = require('redis');
const client = redis.createClient();

client.on("ready", () => {
  console.log("Redis client connected to the server");
});
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
