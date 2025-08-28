import random

num_chars=10
password=""
for index in range(num_chars):
    char_index=random.randint(0,25)
    char_index+=ord('a')
    password+=chr(char_index)
print(password)