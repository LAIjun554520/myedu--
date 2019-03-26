import os

def os_demo():
    # 获取当前目录
    getcwd = os.getcwd()
    print(getcwd)
    # 获取上级目录路径
    abspath = os.path.abspath('..')
    print(abspath)
    # 获取上上级目录路径
    abspath1 = os.path.abspath('../..')
    print(abspath1)



def open_demo1():
    # 相对路径../test.text
    # 绝对路径\Users\Administrator\PycharmProjects\myedu\test.text
    text_io = open('test.text', 'w+')
    text_io.write("xx--xxxxx")


def open_demo2():
     # 相对路径../test.text
     # 绝对路径\Users\Administrator\PycharmProjects\myedu\test.text
     # r代表只读,不可写入
     text_io = open('../test.text', 'r')
     # 读取第一行
     readline = text_io.readline()
     print(readline)
     # 读取所有行 返回一个list对象
     readlines = text_io.readlines()
     print(readlines)



if __name__ == '__main__':
    # os_demo()
    # open_demo2()

    pass

