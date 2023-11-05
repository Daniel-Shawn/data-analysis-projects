"""
    #A python code for a number guessing game
    Build a Number guessing game, in which the user selects a range.
    Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
    Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
"""
import random
import math

usr_name = input("Enter your name: ")
print(f"Welcome to the game, {usr_name}!")
range_start = int(input("Type your lower limit: "))
range_end = int(input("Type your upper limit: "))

guess_count = 1
max_guess_count = 3
system_guess = random.randrange(range_start, range_end)
midway = (range_end - range_start) / 2

while guess_count <= 3:
    usr_guess = int(input("Guess the nuber I picked out from your range: "))
    if usr_guess == system_guess and guess_count == 1:
        print("Congratulations! You got it right in only 1 try")
        break
    elif usr_guess == system_guess:
        print("Congratulations! You got it right!")
        break
    else:
        if usr_guess > midway:
            print(f"That's too high. {guess_count} left")
        elif usr_guess < midway:
            print(f"That's too low. {guess_count} left")
    guess_count += 1
else:
    print(f"You dont have any guesses left. The number was {system_guess}")
