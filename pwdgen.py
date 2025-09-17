import sys
import random

def get_password_length():
    desired_length = 10
    if len(sys.argv) > 1:
        desired_length = int(sys.argv[1])
    return desired_length

number_chars=get_password_length()
    
password=""
for index in range(number_chars):
    # Allow us to generate some  
    # capital letters as well.
    character_index = random.randint(0,52)
    character_index += ord('b')
    password += chr(character_index)
print(password)
