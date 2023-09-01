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

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Log the received message from the channel
client.on('message', (channel, message) => {
  console.log('Received message:', message);
  
  // Unsubscribe and quit if the message is 'KILL_SERVER'
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
