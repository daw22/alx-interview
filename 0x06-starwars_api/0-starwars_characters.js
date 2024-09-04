#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  let charactersUrls;
  request(url, function (error, response, body) {
    if (!error) {
      charactersUrls = JSON.parse(body).characters;
      printNames(charactersUrls, 0);
    }
  });
}

function printNames (urls, idx) {
  request(urls[idx], function (error, response, body) {
    if (!error) {
      const name = JSON.parse(body).name;
      console.log(name);
      idx += 1;
      if (idx < urls.length) {
        printNames(urls, idx);
      }
    }
  });
}
