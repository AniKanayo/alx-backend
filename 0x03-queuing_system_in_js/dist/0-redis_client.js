"use strict";

var _redis = _interopRequireDefault(require("redis"));
function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }
// Create a Redis client
var client = _redis["default"].createClient();

// Set up event listeners for the Redis client
client.on('connect', function () {
  console.log('Redis client connected to the server');
});
client.on('error', function (error) {
  console.error('Redis client not connected to the server:', error);
});
