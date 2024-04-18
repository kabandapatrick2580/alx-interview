#!/usr/bin/node
const request = require('request');
const theMovieId = process.argv[2];
const theOptions = {
  url: 'https://swapi-api.hbtn.io/api/films/' + theMovieId,
  method: 'GET'
};

request(theOptions, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    printCharacters(characterUrls, 0);
  }
});

function printCharacters(characterUrls, index) {
  request(characterUrls[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characterUrls.length) {
        printCharacters(characterUrls, index + 1);
      }
    }
  });
}
