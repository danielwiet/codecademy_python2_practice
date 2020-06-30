'''
Rock, Paper, Scissors, NUKE!!
Feeling lucky?
'''

from random import randint
from time import sleep

options = ['ROCK', 'PAPER', 'SCISSORS']

secret_weapon = ['APPLE', 'PEAR', 'BANANA']

message = {
  'tie': "Yawn, it's a tie",
  'won': 'Yay, you won!',
  'lost': 'Oh no, you lost'
}

def decide_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print(message['tie'])
  elif user_choice == 'ROCK' and computer_choice == 'SCISSORS':
    print(message['won'])
  elif user_choice == 'PAPER' and computer_choice == 'ROCK':
    print(message['won'])
  elif user_choice == 'SCISSORS' and computer_choice == 'PAPER':
    print(message['won'])
  elif user_choice in secret_weapon and computer_choice in options:
    print('You have defeted the monster')
  else:
    print(message['lost'])

def play_rps():
  user_choice = raw_input('Enter Rock, Paper, or Scissors  \n')
  user_choice = user_choice.upper()
  sleep(1)
  print('You chose %s' % user_choice)
  sleep(1)
  computer_choice = options[randint(0, 2)]
  print('Your opponent chose %s' % computer_choice)
  sleep(1)
  decide_winner(user_choice, computer_choice)

play_rps()
