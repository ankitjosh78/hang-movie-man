# hang-movie-man

Hangman but for movies 😉

This is a fun hangman style game to guess random movie names from the local database and show some summary about the movie with a link to the same.
# How to use?
Clone the repo, and run "python main.py".

# FAQ:

## What is the movieman.db file?
Movieman.db is the local sqlite database which is used for the functioning of the game. 

At this time it has around 2700 entries , but new entries can be easily added.

## How to add more movies to the database ?

To add new movies just run "python fillingData.py" and give the number of movies you want.

(NOTE: You will need to download the "imdbpy" python module.)

## How does the fillingData.py file works?
It asks you for the number of new entries to be added and then,

It will generate a random sequence and check if a IMDb movie exists with that id in IMDB. 

If found, it will check if there already exists a record for it.

If there is none, then it will added as a new entry to the database and the counter will be increased.

## Example video showing how to play the game:
https://user-images.githubusercontent.com/62146611/125195082-ba513c80-e271-11eb-9c2c-3c223f0c524e.mp4

## Example video showing how to add new movies to the database:
https://user-images.githubusercontent.com/62146611/125195132-f6849d00-e271-11eb-9ba6-61104d568d01.mp4





