cars = ['audi', 'bmw', 'subaru', 'totota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = 17;
if age >= 18:
    print('You are old enough to vote!')
else:
    print('Sorry you are too young to vote')

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your administrator cost is $10")

available_toppings = ['mushrooms', ' olives', 'green peppers', 'pepperoni', ' pineapple', ' extra chesse']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + ".")
print("\nFinished making your pizza！")

