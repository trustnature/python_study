"""
学习IO操作
"""
filename = 'pi_digits.txt'
"""
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I Love Programming.\n")
    file_object.write("I Love creating new games.\n")








