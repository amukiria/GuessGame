# Guess a number game
import random

print('hello. what is your name?')
name = input()

print('well ' + name + ' I am thinking of a number btwn 1 and 20')
secretNumber = random.randint(1, 20)

# print('DEBUG: Secret Number is ' + str(secretNumber))

for guessesTaken in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break # correct guess

if guess == secretNumber:
    print('well done ' + name + ' you guessed my number in ' + str(guessesTaken) + ' guess')
else:
    print('the number I was thinking of was ' + str(secretNumber))


