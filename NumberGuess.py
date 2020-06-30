'''
Number Guess
Let's play some dice! Feeling lucky?
'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input('Guess a number: '))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = (number_of_sides * 2)
  print('The maximum possible value is %d' % max_val)
  guess = get_user_guess()
  if guess > max_val or guess == 1:
    print('Your guess is invaid')
    return
  else:
    print('Rolling...')
    sleep(2)
    print('The first roll is: %d' % first_roll)
    sleep(1)
    print('The second roll is: %d' % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print('The total value of the rolls is: %d' % total_roll)
    print('The result is...')
    sleep(1)
    if guess == total_roll:
      print('Winner, winner, chicken dinner!')
    else:
      print('This aint your lucky day my friend')

roll_dice(6)