'''
RGB converter to hexadecimal
you got this
'''
from time import sleep

def rgb_hex():
  invalid_msg = 'Ya dummy, that\'s not right'
  red = int(raw_input('Please enter a red value: \n'))
  if red > 255 or red < 0:
    print(invalid_msg)
    return
  green = int(raw_input('Please enter a green value \n'))
  if green > 255 or green < 0:
    print(invalid_msg)
    return
  blue = int(raw_input('Please enter a blue value \n'))
  if blue > 255 or blue < 0:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print( '%s' % (hex(val)[2:].upper()))

def hex_rgb():
  invalid_msg = 'Ya dummy, that\'s not right'
  hex_val = raw_input('Please enter the hexadecimal you want to convert: \n')
  if len(hex_val) != 6:
    print(invalid_msg)
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  
  red = hex_val % two_hex_digits

  print('Red is %s, Green is %s, Blue is %s' %(red, green, blue))


def converter():
  while True:
    option = raw_input(
      'Enter 1 to convert RGB to HEX \nEnter 2 to convert HEX to RGB \nEnter X to EXIT: \n'
    )
    if option == '1':
      print('RGB to HEX...')
      rgb_hex()
    elif option == '2':
      print('Hex to RGB...')
      hex_rgb()
    elif option == 'X' or option == 'x':
      print('Fine, be that way')
      sleep(2)
      print('jerk...')
      sleep(1)
      break
    else:
      print('Uhh, error encountered?')

converter()















