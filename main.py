""" importing required modules """

from random import choice
import sqlite3

""" making connection to the local database """

db  =  sqlite3.connect("movieman.db")

mc = db.cursor()

# fetching all the distinct genres from the database
mc.execute("select distinct genre from movies order by genre asc")

genres = mc.fetchall()
newGen = []

# storing the genres in the newGen variable
for x in genres:
    newGen.append(x[0])

# fetching all the distinct genres from the database
mc.execute("select distinct language from movies order by language asc")

languages = mc.fetchall()
newLang = []
# storing the languages in the newLang variable
for x in languages:
    newLang.append(x[0])

""" Displaying the user a choice before starting the game """

print("1. Completely random movie.")
print("2. Movie from specific genres like (Action, Fantasy)")
print("3. Movie from specific language like (English, Spanish)")

try:

    # storing user's initial choice
    userChoice = int(input("How do you want to guess the movie?"))

except ValueError as _:

    print("Please enter a correct number and try again.")
    quit()

# If user wants movies from specific genres 

if userChoice  ==  2:

    print("Select any genre that you want:")
    count = 1

    for genre in newGen:
        print(count,":",genre)
        count += 1

    try:

        # storing user's genre choice
        genreChoice = int(input("Enter your choice:"))

        # doing some checks
        if genreChoice > count or genreChoice < 1:

            print("Please enter a proper number from the given list and try again")
            quit()

    except ValueError as _:

        print("Please enter a number from the given list and try again.")
        quit()

    # a dictionary to store genre names with their respective code number
    genreMap = {}
    count = 1
    for genre in newGen:
        genreMap[count] = genre
        count += 1

    targetGenre = genreMap[genreChoice]

    print(targetGenre)
    mc.execute("select movieID from movies where genre= ? order by movieID asc",(targetGenre,))

    # a list of all the movieIDs from that specific genre
    movieIDs = []
    for x in mc.fetchall():
        movieIDs.append(x[0])

# If user wants movies from specific languages 

elif userChoice  ==  3:

    print("Select any language that you want:")
    count = 1

    for language in newLang:
        print(count,":",language)
        count += 1
    print()
    print("(NOTE: You can scroll up or down to see more languages.)")
    try:

        # storing user's language choice
        languageChoice = int(input("Enter your choice:"))

        # doing some checks
        if languageChoice > count or languageChoice < 1:

            print("Please enter a proper number from the given list and try again")
            quit()

    except ValueError as _:

        print("Please enter a number from the given list and try again.")
        quit()

    # a dictionary to store languages with their respective code number
    langMap = {}
    count = 1
    for lang in newLang:
        langMap[count] = lang
        count += 1

    targetLanguage = langMap[languageChoice]
    print(targetLanguage)
    mc.execute("select movieID from movies where language= ? order by movieID asc",(targetLanguage,))

    # a list of all the movieIDs from that specific language
    movieIDs = []
    for x in mc.fetchall():
        movieIDs.append(x[0])

# If user wants movies to be completely random

elif userChoice == 1:

    mc.execute("select distinct movieID from movies order by movieID asc")

    # a list of all the movieIDs from that specific genre
    movieIDs = []
    for x in mc.fetchall():
        movieIDs.append(x[0])

# If wrong choice

else:

    print("Please select correct option and try again.")
    quit()

""" Selecting a random movie from the list and getting all details about it """

movieID = choice(movieIDs)

# Storing movieName
mc.execute("select movieName from movies where movieID=?",(movieID,))

for x in mc.fetchall():
    movieName = x[0]

# Storing movieSummary
mc.execute("select movieSummary from movies where movieID=?",(movieID,))
for x in mc.fetchall():
    movieSummary = x[0]

# Closing the connnection
db.close()

# Storing the original movie name in a variable
actualMovie = movieName

# Movie name in string and it's length
movieName = movieName.lower()
movieLen = len(movieName) 

# Movie Link
movieLink = "https://www.imdb.com/title/tt"

movieLink = movieLink + "0"*(7-len(str(movieID))) + str(movieID)

""" Implementation of the actual game starts from here """

# Using a hashmap to store all characters of the movie
hashMap = {}
for x in movieName:
    hashMap[x] = False

# Printing hints about the movie title
print("Okay so your movie is now ready, it is",movieLen,"characters long with",movieName.count(" "),"spaces, ...you have 8 tries to guess the movie.")

# Asking the user for choice
choice =  input("Do you want to start guessing? (y/n)") 

# If choice is "no"
if choice.lower()  == "n":

    print("FUCK YOU FOR WASTING MY TIME")

# If choice is not "no"
else:

    # No of tries.
    tries = 8

    # Checking if all the tries are used.
    while tries > 0 :

        # Using a flag to check for values in our hashMap
        flag = 0

        for x in hashMap:

            if hashMap[x] == False:
                flag=1

        if flag == 0:

            print()
            print("Congratulations, you have succesfully guessed the movie:",actualMovie)
            break

        # Guessing the letter and doing checks
        character_guessed = input("Enter the next letter of the movie:").lower()

        # If guess was correct
        if character_guessed in movieName and len(character_guessed) == 1:

            # If already guessed this
            if hashMap[character_guessed] == True:

                print("You have already guessed this.")
                continue

            # If not guessed before
            else:

                hashMap[character_guessed] = True
                for c in movieName:
                    if hashMap[c] == True:
                        print(c,sep = '',end = '')
                    else:
                        print('_',sep = '',end = '')
                print()

        # If guess is incorrect
        else:

            print("Your guess was incorrect, you have",tries-1,"tries left.")
            tries -= 1

    # If all the tries are over.
    if flag == 1:

        print()
        print("You have lost the game...the movie was:", actualMovie)
        print()

    # Printing a short summary about the movie
    print("Here's a short summary of the movie:")
    print()
    print(movieSummary)
    print("To learn more about the movie, you can go to:",movieLink)
    print("BYE!")
