#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) console.log(err);
  let list = [];
  for (const film of JSON.parse(body).results) {
    list = list.concat(film.characters);
  }
  const uniq = list.filter(x => x.includes('18'));
  console.log(uniq.length);
});
