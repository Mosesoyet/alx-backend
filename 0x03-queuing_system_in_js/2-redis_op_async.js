#!/usr/bin/node
/**
 * Creates a new a connection to redis server
 *
 */
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
	console.log("Redis client not connected to the server:", err.toString());
});

client.on('connect', () => {
	console.log("Redis client connected to the server");
});

function setNewSchool( schoolName, value ) {
	console.log(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
	console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
