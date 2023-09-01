import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get and set functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  try {
    const reply = await setAsync(schoolName, value);
    console.log('Reply:', reply);
  } catch (error) {
    console.error('Error setting value:', error);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(schoolName);
    if (reply === null || reply === undefined) {
      console.log('Value not found');
    } else {
      console.log(reply);
    }
  } catch (error) {
    console.error('Error getting value:', error);
  }
}

// Use async IIFE to properly sequence the async functions
(async function() {
  await displaySchoolValue('School');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
