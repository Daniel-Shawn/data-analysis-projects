"""
    Hangman guessing game!!!!

The Hangman program randomly selects a secret word from a list of secret words. The player gets limited chances to win
the game. When a letter in that word is guessed correctly, that letter position in the word is made visible. In this
 way, all letters of the word are to be guessed before all the chances are over.

 For convenience, chances = have given length of word + 2.
"""


import random, re
from collections import Counter

word_list = ['mug', 'trains', 'steam', 'young', 'permit', 'prepare', 'marvelous', 'join', 'correct', 'exist', 'raspy', 'next', 'ignorant', 'wooden', 'noxious', 'sugar',
             'wax', 'crime', 'honey', 'strip', 'superb', 'yielding', 'squeal', 'copy', 'demonic', 'dam', 'moon',
             'safe', 'wanting', 'shoe', 'guard', 'sin', 'spray', 'finicky', 'release', 'thirsty', 'striped', 'snatch',
             'blue', 'thank', 'war', 'basket', 'grass', 'chase', 'nutritious', 'crayon', 'desire', 'distinct', 'self',
             'drink', 'fascinated', 'feeling', 'offbeat', 'mushy', 'encouraging', 'bag', 'rifle', 'expect', 'sidewalk', 'thick']

system_guess = random.choice(word_list)
chances = len(system_guess) + 2
print(f"Word: {system_guess}")
print(f"Welcome player to The Hangman Game!! You have {chances} chances")
i = 1

playing = True
score = 0
word_string = ''
while i <= chances and playing is True:
    user_guess = input("Your guess: ")
    if user_guess.isdigit():
        print('Input letters only!')
        playing = False
        chances = 0
        break

    if len(user_guess) > 1:
        print('Enter 1 letter at a time only!!!')
        chances -= 1
        continue
    else:
        if user_guess.isdigit():
            print('Input letters only!')
            playing = False
            chances -= 1
        else:
            if user_guess in system_guess:
                word_count = system_guess.count(user_guess)
                for _ in range(word_count):
                    word_string += user_guess

                for char in system_guess:
                    if char in user_guess and (Counter(user_guess) != Counter(system_guess)):
                        print(char, end=' ')
                    elif Counter(user_guess) == Counter(system_guess):
                        print("The word is:", end=' ')
                        print(system_guess)
                        print('Congratulations, You won!')
                        break
                    else:
                        print('_', end=' ')


if playing is False and chances <= 0:
    print("Game Over!")






