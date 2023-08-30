import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

function setNewSchool(schoolName, value) {
  // Set the value for the key in Redis
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.error('Error setting value:', error);
    } else {
      console.log('Value set:', reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  // Get the value for the key from Redis
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.error('Error getting value:', error);
    } else {
      console.log('Value:', reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
