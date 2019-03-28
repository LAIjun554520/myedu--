# 面向对象编程

# class  类
# object 对象或者所有类的父类
# self:就代表类本身


# 声明类的语法class:就是声明一个类;()里面的填写这个类的父类
class Human(object):
    # 类的初始化方法
    def __init__(self,name,age,sex):
        # 将入参的name 赋值给类本身的name
        self.name=name
        self.age=age
        self.sex=sex
    # 类里面的方法,必传self
    def myinfo(self):
        print('我叫%s,我今年%s,%s'%(self.name,self.age,self.sex))

    def myinfostr(self):
        return'我叫%s,我今年%s,%s'%(self.name,self.age,self.sex)

# 声明一个测试者类继承 human 类
class Tseter(Human):


    def ZhiXingCeShi(self):
        # 调用父类的属性
        print(self.name)




        print('我在执行测试,别打扰我')
        # 调用父类的方法
        self.myinfo()






if __name__ == '__main__':
    # = 后面 调用了这个类 传入 初始化的参数 参数必须传,而且传完整
    # = 前面是对象名
    # 对象是类的实例化
    #
    # human = Human('laijun', 23, 'nan')
    # print(type(human))
    # human.myinfo()
    #
    # myinfostr = human.myinfostr()
    # print(myinfostr)
    # 要先传参,才能封装对象,调用方法
    tseter = Tseter("LAIJUN", 25, "男")
    tseter.ZhiXingCeShi()