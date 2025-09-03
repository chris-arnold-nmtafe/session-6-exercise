import sys
import random

number_chars = 10
if len(sys.argv) > 1:
    number_chars = int(sys.argv[1])
password=""
for index in range(number_chars):
    # Allow us to generate some  
    # capital letters as well.
    character_index = random.randint(0,52)
    character_index += ord('b')
    password += chr(character_index)
print(password)
