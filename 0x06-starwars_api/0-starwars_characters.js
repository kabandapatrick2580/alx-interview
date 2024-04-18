#!/usr/bin/node
const request = require('request');

// Movie ID provided as the first positional argument
const movieId = process.argv[2];

// URL of the Star Wars API
const apiUrl = `https://intranet.alxswe.com/swapi/api/films/${movieId}/`;

// Make a GET request to the API endpoint to fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  try {
    // Parse the JSON response body
    const movieData = JSON.parse(body);

    // Extract the characters array from the movie data
    const characters = movieData.characters;

    // Iterate over each character and print their name
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Error:', `Failed to fetch character details. Status code: ${response.statusCode}`);
          return;
        }

        try {
          // Parse the JSON response body
          const characterData = JSON.parse(body);
          
          // Print the character's name
          console.log(characterData.name);
        } catch (error) {
          console.error('Error:', error);
        }
      });
    });
  } catch (error) {
    console.error('Error:', error);
  }
});
