# study
message = "Hello python World !"
print(message.title())
print(message.upper())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("language\n\tPyton")
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
print(0.2+0.1)
print(3/2)
age = 23
message = "Happy " + str(age) + "rd Birthiday"
print(message)
bicycles = ['trek', 'cannondale', 'redline']
bicycles[1] = 'ducati'
bicycles.append('duca')
bicycles.insert(0,'hlwe')
del bicycles[0]
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print(len(cars))
print(cars[-1])
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick\n")
print("Thank you ,everyone.That was a great magic show@")
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squars = []
for value in range(1,11):
    squars.append(value**2)
print(squars)
digits = [1, 2, 3, 4, 5, 6]
print(min(digits))
print(max(digits))
print(sum(digits))
squars = [value**2 for value in range(1,11)]
print(squars)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[2:])
print(players[-2:])
for player in players[:3]:
    print(player.title())
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorits foods are:")
print(my_foods)
print("\nMy frined's favorite foods are:")
print(friend_foods)





