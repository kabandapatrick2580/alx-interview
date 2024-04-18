#!/usr/bin/node
const https = require('https'); // Use https for secure communication
const request = require('request'); // Assuming request is installed (npm install request)

const baseUrl = 'https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg/films/';
const movieId = process.argv[2]; // Assuming movie ID is the second argument

function getCharacterNames(movieId) {
  const url = `${baseUrl}${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API request failed:', response.statusCode);
      return;
    }

    try {
      const data = JSON.parse(body);
      const characters = data.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error('Error fetching character data:', characterError);
            return;
          }

          if (characterResponse.statusCode !== 200) {
            console.error('API request failed (character):', characterResponse.statusCode);
            return;
          }

          try {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          } catch (parseError) {
            console.error('Error parsing character data:', parseError);
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing movie data:', parseError);
    }
  });
}

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
} else {
  getCharacterNames(movieId);
}
