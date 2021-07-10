from random import choice
import sqlite3

db=sqlite3.connect("movieman.db")

mc=db.cursor()

mc.execute("select distinct genre from movies order by genre asc")

genres=mc.fetchall()
newGen=[]
for x in genres:
    newGen.append(x[0])


print("1. Completely random movie.")
print("2. Movie from specific genres like (Action, Fantasy)")
userChoice=int(input("How do you want to guess the movie?"))

if userChoice == 2:

    print("Select any genre that you want:")
    count=1
    for genre in newGen:
        print(count,":",genre)
        count+=1

    genreChoice=int(input("Enter your choice:"))

    genreMap={}
    count=1
    for genre in newGen:
        genreMap[count]=genre
        count+=1

    targetGenre=genreMap[genreChoice]

    mc.execute("select movieID from movies where genre= ? order by movieID asc",(targetGenre,))

    movieIDs=[]
    for x in mc.fetchall():
        movieIDs.append(x[0])

else:

    mc.execute("select distinct movieID from movies order by movieID asc")
    movieIDs=[]
    for x in mc.fetchall():
        movieIDs.append(x[0])

movieID=choice(movieIDs)

mc.execute("select movieName from movies where movieID=?",(movieID,))

for x in mc.fetchall():
    movieName=x[0]

mc.execute("select movieSummary from movies where movieID=?",(movieID,))
for x in mc.fetchall():
    movieSummary=x[0]

# Closing the connnection
db.close()

actualMovie=movieName
movieName=movieName.lower()
movieName.replace("'","")
# Movie name in string and it's length
movieLen=len(movieName) 

# Movie Link
movieLink="https://www.imdb.com/title/tt"
movieLink+="00"+str(movieID)

""" Using a hashmap to store all characters of the movie """
hashMap={}
for x in movieName:
    hashMap[x]=False

# Print dialog
print("Okay so your movie is now ready, it is",movieLen,"characters long with",movieName.count(" "),"spaces, ...you have 8 tries to guess the movie.")
# Asking the user for choice
choice= input("Do you want to start guessing? (y/n)") 

# If choice is "no"
if choice.lower() =="n":
    print("FUCK YOU FOR WASTING MY TIME")

# If choice is not "no"
else:

    # No of tries.
    tries=8

    # Checking if all the tries are used.
    while tries > 0 :

        """ Using a flag to check for values in our hashMap """
        flag=0
        for x in hashMap:
            if hashMap[x]==False:
                flag=1
        if flag==0:
            print("Congratulations, you have succesfully guessed the movie:",actualMovie)
            break

        """ Guessing the letter and doing checks """
        character_guessed=input("Enter the next letter of the movie:").lower()

        # If guess was correct
        if character_guessed in movieName and len(character_guessed)==1:

            # If already guessed this
            if hashMap[character_guessed]==True:
                print("You have already guessed this.")
                continue

            # If not guessed before
            else:
                hashMap[character_guessed]=True
                for c in movieName:
                    if hashMap[c]==True:
                        print(c,sep='',end='')
                    else:
                        print('_',sep='',end='')
                print()

        # If guess is incorrect
        else:
            print("Your guess was incorrect, you have",tries-1,"tries left.")
            tries-=1

    # If all the tries are over.
    if flag==1:
        print()
        print("You have lost the game...the movie was:", actualMovie)
        print()
    # Printing a short summary about the movie
    print("Here's a short summary of the movie:")
    print()
    print(movieSummary)
    print("To learn more about the movie, you can go to:",movieLink)
    print("BYE!")
