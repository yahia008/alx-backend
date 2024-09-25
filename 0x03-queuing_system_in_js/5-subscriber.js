import { createClient } from 'redis';

const redisClient = createClient();

//Connect to the Redis server.
redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

//Join the Holberton School channel.
redisClient.subscribe('holberton school channel');

//Listen for messages on the channel and print the message upon receipt.
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
//Unsubscribe from the channel and terminate the server connection.
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
