""" importing required modules """

from imdb import IMDb
from imdb import IMDbDataAccessError
from random import choice
import sqlite3
from string import digits

""" Asking the user the number of movies they want to add """

counter = int(input("Enter how many new movies you want?(e.g 10)"))
count = 0


""" Initialising the IMDB class and connecting to the local database """

movieman = IMDb()
db = sqlite3.connect("movieman.db")
mc = db.cursor()

""" Checks for no of movies added and adding new movies """
while counter > 0:

    # generating a sequence
    sequence = "00"
    for _ in range(5):
        sequence += choice(digits)

    # Trying to get a movie with a uniqueID equal to our generated sequence
    try:

        movie = movieman.get_movie(sequence)

        try:

            # Getting the genres of the movie
            genres = movie['genres']
            movieID = int(sequence)

            # Checking if there already a exists a movie with the same id
            mc.execute(f"select count(distinct movieID) from movies where movieID={movieID}")
            answer = mc.fetchall()

            # If there are no duplicates then proceeding
            if answer[0][0] == 0:

                flag = 0
                movieName = str(movie)
                movieSummary = str(movie.summary())

                for genre in genres:
                    sqlQuery = "insert into movies values ( ?, ?, ?,?)"
                    try:

                        # Inserting values into the movies table in the database
                        mc.execute(sqlQuery,(movieID,movieName,genre,movieSummary))
                        db.commit()
                        flag=1

                    except sqlite3.ProgrammingError as e:
                        pass
                    
                if flag == 1:
                    
                    # Decreasing the counter variable 
                    counter-=1 

                    #Count variable used to show the total movies added so far
                    count+=1
                    print(count,"new movies added to the database.")

        except KeyError as _:

            pass
        except IMDbDataAccessError as _:

            pass
    except IMDbDataAccessError as e:

        pass

# Closing the connection when done
db.close()
