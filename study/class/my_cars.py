"""
导入整个模块
"""
import cars

my_beetle = cars.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = cars.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())