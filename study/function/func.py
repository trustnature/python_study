# 测试基本的函数
"""
def greet_user():
    print("Hello")


greet_user()


# 没有多态
def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user("jesse")


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'wille')


def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamset', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='wiliie',animal_type='cat')
"""

"""
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix','lee')
print(musician)


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix',age=27)
print(musician)


def greet_formatted_name(first_name, last_name):
    #返回整洁的姓名
    full_name = first_name + ' ' + last_name
    return full_name


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit")

    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if(l_name == 'q'):
        break
    formatted_name = greet_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
"""

"""
def greet_users(names):
    # 向列表中的每位用户都发出简单的问题
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def print_models(unprinted_designs, complete_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Print model: " + current_design)
        complete_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedon']
completed_models = []


print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
"""


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(15,'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field = 'physics')
print(user_profile)

"""
    每个函数都应该包含简要的阐述其功能的注释，该注释应紧跟在函数定义后面
    给形参指定默认值时，等号两边不要有空格 def function_name(paramter_1='default value')
    如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
"""


