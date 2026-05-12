"""

练习11-3:雇员
编写一个名为Employee 的类，其方法__init__()接受名、姓和年薪，并将它们存储在属性中。编写一个名为 give_raise()的方法，它默认将年薪增加5000美元，
但也能够接受其他的年薪增加量。为 Employee 编写一个测试用例，其中包含两个测试方法:test_give_default_raise()和
test_give_custom_raise()使用方法setUp()，以免在每个测试方法中都新建雇员实例。运行这个测试用例，确认两个测试都通过了。

"""

import unittest

from test import Employee

class TestEmployee(unittest.TestCase):
    # setUp方法：不用每次都重新实例化新对象
    def setUp(self):
        # 能实例化多个对象
        self.xiaoming = Employee('小明', '张', 10000)
        self.xiaohong = Employee('小红','李',15000)

    # 每个测试用例独立
    def test_give_default_raise(self):
        # xiaoming = Employee('小明', '张', 10000)
        self.xiaoming.give_raise()
        self.assertEqual(self.xiaoming.salary,15000)

    # 每个测试用例独立
    def test_give_custom_raise(self):
        self.xiaohong.give_raise(10000)
        self.assertEqual(self.xiaohong.salary,25000)


"""
结果：

(base) ➜  作业 git:(main) ✗ python -m unittest
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

"""

