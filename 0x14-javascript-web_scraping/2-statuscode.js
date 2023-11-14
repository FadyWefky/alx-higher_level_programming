#!/usr/bin/node
// Display get
const request = require('request');

request(process.argv[2], function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', data.statusCode);
  }
});
