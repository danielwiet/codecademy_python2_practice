"""
This program will calculate the area of a circle or triangle
"""

print('The calculator is starting up')

option = raw_input('Enter C for Circle, T for Triangle: ')

if option == 'C' or option == 'c':
  radius = float(raw_input('Enter the radius: '))
  area = round(3.14159 * (radius ** 2), 2)
  print('The area of the circle with a radius of ' + str(radius) + ' is ' + str(area))

elif option == 'T' or option == 't':
  base = float(raw_input('Enter the base: '))
  height = float(raw_input('Enter the height: '))
  area = round((.5 * base * height),2)
  print('The area of a triangle with base %f and height %f is %f' % (base, height, area))

else:
  print('You entered an option that is not available.')
  print('Please run the program again and choose a valid option')