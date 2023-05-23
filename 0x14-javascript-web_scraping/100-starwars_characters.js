#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, content) {
  if (!err) {
    const characters = JSON.parse(content).characters;
    characters.forEach((character) => {
      request(character, function (err, response, content) {
        if (!err) {
          console.log(JSON.parse(content).name);
        }
      });
    });
  }
});
