import sys
import random

num_chars=10
if len(sys.argv)>1:
    num_chars=int(sys.argv[1])
password=""
for index in range(num_chars):
    #Allow us to generate some 
    #capital letters too.
    char_index=random.randint(0,52)
    char_index+=ord('b')
    password+=chr(char_index)
print(password)