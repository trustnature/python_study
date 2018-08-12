import json

numbers = [2, 3, 5, 7, 11]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

username = input("What is your name?")

filename = 'username.json'
"""
with open(filename,'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
"""

try:
    with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError
    username = input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back," + username + "!")


