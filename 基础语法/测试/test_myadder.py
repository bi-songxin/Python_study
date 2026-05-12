import unittest

# 被测试.py在同一文件夹下
# 使用from 文件名 import 函数名  或  from 文件名 import 类名

from my_adder import my_adder

# 继承unittest.TestCase的属性和方法
class MyTest(unittest.TestCase):
    # 可定义不同的测试用例，每个测试用例都是一个方法，且方法命名必须以test_开头，因为unittest这个方法会自动搜索以test_开头的方法

    # 测试测试用例正数和正数
    def test_positive_with_positive(self):
        # assert my_adder(5,3) == 8

        # assertEqual方法传入的第一个参数和第二个参数是否相等，相等显示测试通过，不相等显示测试不通过
        self.assertEqual(my_adder(5,3), 8)

    # 测试测试用例负数和正数
    def test_negative_with_positive(self):

        self.assertEqual(my_adder(-2,3), 1)

    # 测试测试用例负数和负数
    def test_negative_with_negative(self):
        self.assertEqual(my_adder(-1,-1),-2)
