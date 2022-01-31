"""EX02- One Shot Wordle."""

__author__ = "730312375"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ") #Asking user to input guess for secret_word

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ") #Telling user that guess is not the same length as secret_word 

index: int = 0
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" 

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji = emoji + GREEN_BOX #Adds a green box for indices at which characters match between guess and secret_word
    else:
        exists: bool = False
        alternate_indices: int = 0
        while not exists and alternate_indices < len(secret_word):
            if guess[index] == secret_word[alternate_indices]:
                exists = True
            else:
                alternate_indices = alternate_indices + 1
        if exists:
            emoji = emoji + YELLOW_BOX #Adds a yellow box for places at which letters in guess are in alternate indices of secret_word
        else:
            emoji = emoji + WHITE_BOX #Adds a white box for places at which letters in guess are not in secret_word
    index = index + 1
print(emoji) #Prints concatenated string of emojis

if guess == secret_word:
    print("Woo! You got it!") 
else:
    print("Not quite. Play again soon!")
    