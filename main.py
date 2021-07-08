from random import choice
from imdb import IMDb
from imdb import IMDbError
from string import digits

movieman=IMDb() # initialising the IMDb class.

sequence="00" # generating a unique id for the movie
for _  in range(5):
    sequence+=choice(digits)

movie=movieman.get_movie(sequence) # getting details about the movie

print("Okay so your movie is now ready, it is",len(str(movie)),"characters long with",str(movie).count(" "),"spaces, ...you have 8 tries to guess the movie.")

choice= input("Do you want to start guessing? (y/n)") # Asking the user for choice

if choice.lower() =="n":
    print("FUCK YOU FOR WASTING MY TIME")
else:
    tries=8
    indice=0
    flag=0
    movie_link="https://www.imdb.com/title/tt"
    movie_link+=sequence # making the link
    while tries > 0 :
        if indice == len(str(movie)):
            print("Huraah, you have succesfully guessed the movie.")
            flag=1
            break
        character_guessed=input("Enter the next letter of the movie:").lower()
        if character_guessed == str(movie).lower()[indice]: # guessing the movie
            print("Your guess was correct...")
            indice+=1
        else: # for incorrect guess
            print("Your guess was incorrect....you have",tries-1,"tries left.")
            tries-=1

    if flag==0: # if fails to guess
        print("You have lost the game... the movie was", str(movie))

    # Miscellaneous outputs
    print("Here's a short summary of the movie:")
    print(movie.summary())
    print("To learn more about the movie, you can go to:",movie_link)
    print("BYE!")
