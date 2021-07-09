from random import choice
from imdb import IMDb
from imdb import IMDbError
from string import digits

# initialising the IMDb class.
movieman=IMDb() 

""" Generating unique id for the movie """
sequence="00"
for _  in range(5):
    sequence+=choice(digits)

""" Movie Details """

# Fetching details of the movie
movie=movieman.get_movie(sequence) 

# Movie name in string and it's length
movie_name=str(movie).lower() 
movie_len=len(movie_name) 

# Movie Link
movie_link="https://www.imdb.com/title/tt"
movie_link+=sequence 

""" Using a hashmap to store all characters of the movie """
hashMap={}
for x in movie_name:
    hashMap[x]=False

# Print dialog
print("Okay so your movie is now ready, it is",movie_len,"characters long with",movie_name.count(" "),"spaces, ...you have 8 tries to guess the movie.")

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
            print("Congratulations, you have succesfully guessed the movie:",movie)
            break

        """ Guessing the letter and doing checks """
        character_guessed=input("Enter the next letter of the movie:").lower()

        # If guess was correct
        if character_guessed in movie_name and len(character_guessed)==1:

            # If already guessed this
            if hashMap[character_guessed]==True:
                print("You have already guessed this.")
                continue

            # If not guessed before
            else:
                hashMap[character_guessed]=True
                for c in movie_name:
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
        print("You have lost the game... the movie was:", movie)

    # Printing a short summary about the movie
    print("Here's a short summary of the movie:")
    print(movie.summary())
    print("To learn more about the movie, you can go to:",movie_link)
    print("BYE!")
