# def int_demo():
#     aint = 1
#     print(aint)
#     print(type(aint))
#
#
# def str_demo():
#     str = '2'
#     print(str)
#     print(type(str))
#
# def float_demo():
#     afloat=1.55
#     print(afloat)
#     print(type(afloat))
#
#
# def str_demo1():
#     a='hello'
#     b='world'
#     return a+b
#
#
# def str_demo2():
#     a='hello'
#     b=250
#     s=str(b)
#     print(type(s))
#     print(a+s)
#
#
# def str_demo3():
#     a = 'hello'
#     b = 250
#     print('%s%s'%(a,b))
#
#
#
#
# def add(aint,bint):
#     print(aint)
#     print(bint)
#     return aint+bint
#
# if __name__ == '__main__':
#     add2 = add(1, 2)
#     print(add2)
#
#
#
#
# # if __name__ == '__main__':
#     print(str_demo3())
#     # print(str_demo2())
#     # print(str_demo1())
#     # float_demo()
# int_demo()
# str_demo()


# list
def list_demo():
    alist = [5, 8, 'yy', 'tt', 'uu', 9, 5, 4, 3]
    print(alist[0])
    print(alist[-2])


def list_update(alist):
    alist[0] = 1
    print(alist)


if __name__ == '__main__':
    pass
