# hang-movie-man

Hangman but for movies 😉

This is a fun hangman style game to guess random movie names from the local database and show some summary about the movie with a link to the same.

# How to use?
Clone the repo, and run "python newMain.py".

# FAQ:

## What is the movieman.db file?
Movieman.db is the local sqlite database which is used for the functioning of the game. 

At the time it has around 500 entries , but new entries can be easily added.

## How to add more movies to the database ?

To add a new movie just run "python newDataModel.py" ,

## How does the newDataModel.py file works?
This will generate a random sequence and check if a IMDb movie exists with that id from the IMDb api. 

It might give some error sometimes(very rare) if there exists no movies for that id.

If found, it will check if there already exists a record for it.

If there is none, then it will added as a new entry to the database.

## "Hey, the newDataModel.py file adds only one movie at a time, is there a way to continuously add movies to the database?"

Yes, just run the "script.sh" file if you are using Linux or macOS.

It will keep adding movies unless you close the script using "Ctrl-C".

(If you are still using windows, i dont know what to say 🙂 )
