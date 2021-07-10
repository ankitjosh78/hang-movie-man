from imdb import IMDb
from imdb import IMDbDataAccessError
from random import choice
import sqlite3
from string import digits

counter=int(input("Enter how many new entries you want?(e.g :10)"))
count=counter
while counter > 0:
    sequence="00"
    for _ in range(5):
        sequence+=choice(digits)

    movieman=IMDb()

    db=sqlite3.connect("movieman.db")

    mc=db.cursor()
    try:
        movie=movieman.get_movie(sequence)
        try:
            genres=movie['genres']
            movieID=int(sequence)
            mc.execute(f"select count(distinct movieID) from movies where movieID={movieID}")
            answer=mc.fetchall()
            if answer[0][0] == 0:
                movieName=str(movie)
                movieSummary=str(movie.summary())

                for genre in genres:
                    sqlQuery="insert into movies values ( ?, ?, ?,?)"
                    try:
                        mc.execute(sqlQuery,(movieID,movieName,genre,movieSummary))
                        db.commit()
                        counter-=1
                    except sqlite3.ProgrammingError as e:
                        print(e)
            db.close()
        except KeyError as _:
            pass
    except IMDbDataAccessError as e:
        print("Sorry no official movie from IMDb found for the current random sequence.")
print(count,"new entries have been added to the database")
