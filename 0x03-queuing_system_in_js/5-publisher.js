const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Log the message on connect
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Log the error message on error
client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

// Function to publish message after a given time
function publishMessage(message, time) {
  setTimeout(() => {
    console.log('About to send:', message);
    client.publish('holberton school channel', message);
  }, time);
}

// Call the 'publishMessage' function for different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
