"""EX02 - One Shot Wordle."""

__author__ = "730255959"


secret: str = "python"

guess: str = input("What is your " + (str(len(secret))) + "-letter guess? ")    

while len(secret) != len(guess):     # checking the lengths 
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")

i: int = 0       # variable
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
exist: bool = False    
alt: int = 0

while i < len(secret):               # adding green boxes
    if (secret[i]) == (guess[i]):
        emoji = emoji + GREEN_BOX
        exist = True
    else:
        while not exist and alt < len(secret):     
            if secret[alt] == guess[i]:            # adding yellow boxes
                emoji = emoji + YELLOW_BOX
                exist = True
            alt = alt + 1
    if not exist:
        emoji = emoji + WHITE_BOX         # adding white boxes
    alt = 0
    exist = False        
    i = i + 1

print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")    
