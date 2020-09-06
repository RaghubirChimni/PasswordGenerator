# Raghubir Chimni
# Date: 9/5/2020
# PasswordGenerator.py

import random

maxLength = input('What is the maximum length of the password? ')

numOfPasswords = input('How many passwords would you like? ')

characters = 'abcdefghijklmnopqrstuvwxyz!?.,-*ABCDEFGHIJKLMNOQRSTUVWXYZ0123456789'

password = ''

print()

for j in range(1, eval(numOfPasswords) + 1):
  for i in range(eval(maxLength)):
    password += random.choice(characters)
  print('Password ' + str(j) + ': ' + password)
  password = ''  

print('\n' + 'Thank you for using this program!')
