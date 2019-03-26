# 这是一个注释
# model  模块  就是一个.py的文件 一个文件是一个小模块,如果包内有__init__.py文件,那么他就是一个大模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系 通过 缩进来表示
# class 类,类型
# str string 字符
# 合法标识符(变量名方法名) : 必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感, 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+k  commit 代码
# ctrl+shift+k push代码

# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量 , 并赋值 1
    aint = 1
    # 打印 aint 的值
    print(aint)
    # 打印 aint 的 类型; type(aint): 获取aint的类型
    print(type(aint))


# 声明一个 str_demo 方法
def str_demo():
    # 声明astr变量 , 并赋值 '1'
    astr = '1'
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

    # 不写
    print('--------------')
    astr = 1
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

def str_demo1():
    a= 'hello'
    b= ' world'
    return a+b

def str_demo2():
    a= 'hello '
    b= 250
    print('a=%s b=%s'%(a,b))
    s = str(b)
    print(s)
    print(type(s))
    print(a+s)


# 声明一个add 方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint+bint
    return aint + bint

# 声明一个 float_demo 方法
def float_demo():
    # 声明afloat变量 , 并赋值 1.90
    afloat = 1.90
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的 类型; type(afloat): 获取afloat的类型
    print(type(afloat))


# def str_demo3():
#     a = 'hello'
#     b = 250
#     print('%s%s'%(a,b))




# def add(aint,bint):
#      print(aint)
#     print(bint)
#      return aint+bint

# if __name__ == '__main__':#     add2 = add(1, 2)
#      print(add2)


if __name__ == '__main__':
    str_demo2()
    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量  ctrl+alt+V
    # 调用add方法 传入1, 2,得到返回值 ,赋值给result变量
    # result = add(1, 2)
    # print('1111')
    pass
