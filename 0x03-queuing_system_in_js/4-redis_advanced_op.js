const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Store the hash value using hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display the hash using hgetall with callback
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Hash:', reply);
  }
});
