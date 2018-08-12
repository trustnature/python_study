"""
dictionary 就是 JSON Map
"""
person = {'Name': 'fFord Prefect', 'Gender': 'Male', 'Occupation': 'Researcher'}
print(person)
person['Age'] = 33
print(person)

vowels = ['a', 'e', 'i', 'e', 'u']
word = "milesaee"

found = {}


for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
for k, v in found.items():
    print(k, 'was found', v, 'time(s).')



alien_p = {'color':'green', 'point':5}
print(alien_p['color'])
print(alien_p['point'])
print(alien_p)
alien_p['x_position'] = 0
alien_p['y_position'] = 25
print(alien_p)

alien_o = {}
alien_o['color'] = 'green'
alien_o['points'] = 5
print(alien_o)

alien_o = {'color': 'green'}
print("The alien is " + alien_o['color'] + ".")
alien_o['color'] = 'yellow'
print("The alien is now " + alien_o['color'] + ".")

alien_o = {'color': 'green', 'points': 5}
print(alien_o)
del alien_o['points']
print(alien_o)

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

user_o = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'ferimi'
}
for key, value in user_o.items():
    print("\nKey: " + key)
    print("Value: " + value)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
for language in favorite_languages.values():
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())

alien_o = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_o,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

pizza = {
    'crust': 'thick',
    'toppints': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")
for topping in pizza['toppints']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go']
}
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are :")
    for language in languages:
        print("\t" + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location)

c = dict();
# 空字典返回 {}
print(c)