'''
Calendar program
this is a calendar program
deal with it
'''

from time import sleep, strftime

user_first_name = 'Dan'
calendar = {}

def welcome():
  print('Welcome, %s' % user_first_name)
  print('The calendar is openning. Please wait patiently...')
  sleep(1)
  print('The current date is ' + strftime('%A %B %d, %Y'))
  print('The current time is ' + strftime('%H %M %S'))
  sleep(1)
  print('What would you like to do?')

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input('Enter A to add, U to update, V to view, D to delete, X to exit \n')
    user_choice = user_choice.upper()
    if user_choice == 'V' or user_choice == 'VIEW':
      if len(calendar.keys()) == 0:
        print('The calendar has no events')
      else:
        print(calendar)
    elif user_choice == 'U' or user_choice == 'UPDATE':
      date = raw_input('What date do you want to update? \n')
      update = raw_input('Enter the update \n')
      calendar[date] = update
      # Note: This a very powerful (and possibly dangerous) line of code. It blindly adds the update to the calendar, without checking if the date is valid or if it already exists (which could override things). Remember, this is a basic calendar with limited functionality. Feel free to add to its behavior after you complete the project.
      print('Update successful')
      print(calendar)
    elif user_choice == 'A' or user_choice == 'ADD':
      event = raw_input('Enter the event: \n')
      date = raw_input('Enter date (MM/DD/YYYY): \n')
      if (len(date) > 10 or int(date[6:]) < int(strftime('%Y'))):
        print('An invalid date was entered')
        try_again = raw_input('Would you like to try again? Y/N \n')
        try_again = try_again.upper()
        if try_again == 'Y' or try_again == 'YES':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print('The event has been added')
        print(calendar)
    elif user_choice == 'D' or user_choice == 'DELETE' or user_choice == 'DEL':
      if len(calendar.keys()) == 0:
        print('There\'s nothing to delete, your calendar is empty')
      else:
        event = raw_input('Which event? \n')
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print('Your event has been deleted')
            print(calendar)
          else:
            print('The event was not found or you have entered an incorrect event')
            try_again = raw_input('Would you like to try again? Y/N \n')
            try_again = try_again.upper()
            if try_again == 'Y' or try_again == 'YES':
              continue
            else:
              start = False
    elif user_choice == 'X':
      start = False
    else:
      print('You have entered an invalid command. Smell ya later')
      print('exiting')
      quit()

start_calendar()