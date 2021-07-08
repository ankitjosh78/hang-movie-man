from random import choice
from imdb import IMDb
from imdb import IMDbError
from string import digits

movieman=IMDb() # initialising the IMDb class.

sequence="00" # generating a unique id for the movie
for _  in range(5):
    sequence+=choice(digits)

print(sequence)

movie=movieman.get_movie(sequence) # getting details about the movie
movie_name=str(movie).lower() # movie name
movie_len=len(movie_name) # no of characters in the movie
movie_link="https://www.imdb.com/title/tt"
movie_link+=sequence # making the movie link

hashMap={}

for x in movie_name:
    hashMap[x]=False

print("Okay so your movie is now ready, it is",movie_len,"characters long with",movie_name.count(" "),"spaces, ...you have 8 tries to guess the movie.")

choice= input("Do you want to start guessing? (y/n)") # Asking the user for choice

if choice.lower() =="n":
    print("FUCK YOU FOR WASTING MY TIME")
else:
    tries=8
    while tries > 0 :
        flag=0
        for x in hashMap:
            if hashMap[x]==False:
                flag=1
        if flag==0:
            print("Congratulations, you have succesfully guessed the movie:",movie)
            break
        character_guessed=input("Enter the next letter of the movie:").lower()
        if character_guessed in movie_name and len(character_guessed)==1:
            if hashMap[character_guessed]==True:
                print("You have already guessed this.")
                continue
            else:
                hashMap[character_guessed]=True
            for c in movie_name:
                if hashMap[c]==True:
                    print(c,sep='',end='')
                else:
                    print('_',sep='',end='')
            print()
        else:
            print("Your guess was incorrect, you have",tries-1,"tries left.")
            tries-=1
    if flag==1:
        print("You have lost the game... the movie was:", movie)
    # Miscellaneous outputs
    print("Here's a short summary of the movie:")
    print(movie.summary())
    print("To learn more about the movie, you can go to:",movie_link)
    print("BYE!")
