# 模块 mode
# main 主要的
# print 打印
# def  申明方法
# int  整数
# demo 例子
def int_demo():  # 申明一个变量，变成数值，打印出来
    aint = 1
    print(aint)


# 同一级别，方法名不能一样
def add(aint, bint):  # 申明一个变量，变成数值，打印出来
    print(aint)
    print(bint)
    return aint + bint

    # int_demo()
    # 提取变量
    result = add(1, 2)
    print(result)
    pass


def int_demo():
    aint = 1
    print(aint)


def add(aint, bint):
    print(aint)
    print(bint)
    return aint + bint


if __name__ == '__main__':
    result = add(1, 2)
    print(result)
    pass


def int_demo():
    aint = 1
    print(aint)


# 声明一个人add方法，参数有两个aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint-bint
    return aint - bint


# mian方法
if __name__ == '__main__':
    # 提取变量 ctrl + alt +v
    # 调用add方法
    # 调用add方法，传入1,2得到返回值，赋值给result变量
    result = add(2, 1)
    print(result)
    pass


# 声明一个int_demo的方法
def int_demo():
    # 声明aint变量，并赋值为1
    aint = 1
    # 打印aint的值
    print(aint)
    # 打印aint的类型，type（aint）：获取aint类型
    print(type(aint))


# 声明一个str_demo的方法
def str_demo():
    # 声明astr变量，并赋值为'1'
    astr = '1'
    # 打印astr的值
    print(astr)
    # 打印astr的类型，type（astr）：获取astr类型
    print(type(astr))


# 声明一个float_demo的方法
def float_demo():
        # 声明afloat变量，并赋值为1.55
        afloat = 1.55
        # 打印afloat的值
        print(afloat)
        # 打印afloat的类型，type（afloat）：获取afloat类型
        print(type(afloat))

if __name__ == '__main__':
    float_demo()
    pass