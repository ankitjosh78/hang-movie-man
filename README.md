# hang-movie-man

Hangman but for movies 😉

This is a fun hangman style game to guess random movie names from the local database and show some summary about the movie with a link to the same.

# How to use?
Clone the repo, and run "python main.py".

# FAQ:

## What is the movieman.db file?
Movieman.db is the local sqlite database which is used for the functioning of the game. 

At the time it has around 1230 entries , but new entries can be easily added.

## How to add more movies to the database ?

To add new movies just run "python fillingData.py" and give the number of movies you want.

(NOTE: You will need to download the "imdbpy" python module.)

## How does the fillingData.py file works?
It asks you for the number of new entries to be added and then,

It will generate a random sequence and check if a IMDb movie exists with that id in IMDB. 

If found, it will check if there already exists a record for it.

If there is none, then it will added as a new entry to the database and the counter will be increased.

## Example video showing how to use:

https://user-images.githubusercontent.com/62146611/125160215-63783400-e199-11eb-9ae2-a33c768f6ee1.mp4



