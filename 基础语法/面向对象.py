"""
练习 9.1：餐馆　创建一个名为 Restaurant 的类，为其 __init__() 方法设置两个属性：restaurant_name 和 cuisine_type。
创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，
指出餐馆正在营业。根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'餐厅名:{self.restaurant_name} 烹饪类型:{self.cuisine_type}')
#
#     def open_restaurant(self):
#         print('正在营业！')
#
# nihao = Restaurant('你好','炒饭')
# print(nihao.restaurant_name,nihao.cuisine_type)
# nihao.describe_restaurant()
# nihao.open_restaurant()




"""
练习 9.4：就餐人数　在为练习 9.1 编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为 0。根据这个类创建一个名为 restaurant 
的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印。添加一个名为 set_number_served() 的方法，用来设置就餐人数。调用这个方法并向它传递新的就餐人数，然后再次打印这个值。
添加一个名为 increment_number_served() 的方法，用来让就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

"""

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served #新增

    def describe_restaurant(self):
        print(f'餐厅名:{self.restaurant_name} 烹饪类型:{self.cuisine_type}')

    def open_restaurant(self):
        print('正在营业！')


    def set_number_served(self,new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self,increase_number_served):
        self.number_served += increase_number_served



restaurant = Restaurant('bsx之家','煎炒')
print(f'就餐人数：{restaurant.number_served}')
restaurant.number_served = 100
print(f'就餐人数：{restaurant.number_served}')

restaurant.set_number_served(200)
print(f'就餐人数：{restaurant.number_served}')

restaurant.increment_number_served(50)
print(f'就餐人数：{restaurant.number_served}')



# 继承

"""
练习 9.6：冰激凌小店　冰激凌小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为练习 9.1 或练习 9.4 编写的 Restaurant 类。
这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 的属性，用于存储一个由各种口味的冰激凌组成的列表。
编写一个显示这些冰激凌口味的方法。创建一个 IceCreamStand 实例，并调用这个方法。

"""

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,flavors):
        super().__init__(restaurant_name,'甜品')
        self.flavors = flavors

    def describe_flavors(self):
        print(f'冰淇淋口味有：{self.flavors}')

iceCream_stand = IceCreamStand('bsx',['蓝莓','草莓','香草','巧克力','绿茶'])
iceCream_stand.describe_flavors()
iceCream_stand.describe_restaurant()