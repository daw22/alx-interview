#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  let charactersUrls;
  request(url, async function (error, response, body) {
    if (!error) {
      charactersUrls = JSON.parse(body).characters;
      for (let i = 0; i < charactersUrls.length; i++) {
        const character = await fetch(charactersUrls[i]);
        const charData = await character.json();
        console.log(charData.name);
      }
    }
  });
}
