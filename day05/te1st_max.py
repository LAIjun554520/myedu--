


# 如何使用pytest 做测试
# 1.设置pycharm
# 2.新建模快以test_ 开头
# 3.新建类 以Test 开头
# 4.在类中新建方法 以test_ 开头

# @ 开头的都叫装饰器


import allure
@allure.feature("类上的装饰器")



class Testlaijun:

    @allure.feature("max方法上的")
    def test_max(self):
        assert 1 < 2

    @allure.feature("max1方法上的")
    def test_max1(self):
        assert 3 > 2

    @allure.feature("max2方法上的")
    def test_max2(self):
        assert 5 < 2

    @allure.feature("max3方法上的")
    def test_max3(self):
        assert 7 <32
