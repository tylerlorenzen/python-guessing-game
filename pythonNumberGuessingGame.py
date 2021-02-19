#Guessing the Random Number Game. 
import random
import time
import numpy as np
import sys

#Delay printing
def delay_print(s):
  #print one character at a time
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)

print('Hello and welcome to my Random Number game! What is your name?')
name = input()


print(f'Welcome {name}, I am thining of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
  print('Take a guess.')
  guess = int(input())

  if guess < secretNumber:
    print('Your guess is too low!')
  elif guess > secretNumber:
    print('Your guess is too high!')
  else:
    break # This condition is for the correct guess

if guess == secretNumber:
  print(f'Good job {name}! You guessed the number in {str(guessesTaken)} guesses!')
else:
  print(f'Nope. The number was thinking of was {secretNumber}')



delay_print(f'\n\nThanks for playing my Random Number Game! Checkout some of my other stuff at tylerlorenzen.tech! \n\nThanks,\n\nTyler!')


# This is another way to do it. 
#def guess(x):
#  random_number = random.randint(1, x)
#  guess = 0
#  while guess != random_number:
#    guess = int(input(f'Guess a number between 1 and {x}: '))
#    if guess < random_number:
#      print('Sorry, guess again. Too low.')
#    elif guess > random_number:
#      print('Sorry, guess again. Too high.')
#  
#  print(f'Yay, congrats! You won!)
