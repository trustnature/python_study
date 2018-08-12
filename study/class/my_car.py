# 打开模块Cars 并导入其中的Car,ElectricCar类
from cars import Car, ElectricCar
# from module_name import * 导入模块中的每个类 不推荐
#  多个模块的话 一次from 即可

my_beetle = Car('vlokswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

