
from day01 import list



def add_demo():
    aint = 20
    bint = 10
    aint_bint = aint + bint
    return aint_bint

def add_demo1(aint,bint):
    print(aint)
    print(bint)
    aint_bint = aint + bint
    return aint_bint

def str_demo():
    a = 'hello'
    b = 1314
    print(a + str(b))
    print('%s%s' %(a,b))


blist=[1,8,3,5,56,99]

def list_demo():
    alist= [9,5,8,3,4,566,5]
    print(alist[1])
    print(alist[-3])
    print(blist[0])
    print(blist[-4])



def list_update(alist):
    alist[0]=55
    print(alist[0])
    print(alist)

    blist[-2]=999
    print(blist[-2])
    print(blist)


def pop_demo(alist):
    alist.pop()
    print(alist)
    alist.pop(3)
    print(alist)
    blist.pop()
    print(blist)
    blist.pop(-2)
    print(blist)


def adict_demo1():
    adict={'name': 'ysl', 'pwd': '123456'}
    adict['name']
    print(adict['name'])

    adict.pop('name')
    print(adict)

list={'11','22','33','44','55'}
def xunhuan_demo(list):
    list = {'11', '22', '33', '44', '55'}
    # for i in range(5):
    #     print('hollo,world')
    #
    # for i in range(3,9):
    #     print(i)
    #
    # for i in range(9,2,-2):
    #     print(i)

    list = {'11', '22', '33', '44', '55'}
    # for i in list:
    #     print(i)


    for i in list:
        print(i)
        print(list[i])


def zuihuo():
    astr = {'山东分行公司'}
    try:
        assert '你'  in astr
    except:
        print('1314')

    print('------------')


def break_demo():
    for i in range(5):
        print(i)
        if i ==3 :
            break
        print('第%s次循环至最后一行代码\n'%i)


def continue_demo():
    for i in range(5):
        print(i)
        if i ==3 :
            continue
        print('第%s次循环至最后一行代码\n'%i)








if __name__ == '__main__':
    continue_demo()

    # break_demo()
    # zuihuo()
    # assert 2 > 4

    # assert 4>2

    # astr = {'山东分行公司'}
    #
    # # assert '你' in astr
    # assert '你' not in astr

    # a = True
    # if True :
    #     print('asd')
    # if False:
    #     print('asdf')
    #
    # a = 0
    # if a> 3:
    #     print(1)
    # elif a >5:
    #     print('sflg')
    # elif a==5:
    #     print('fgjd')
    # else:
    #     print(123)


    # a=0
    # while a<5:
    #     print('123456')
    #     a+=1




    # adict = {'name': 'ysl', 'pwd': '123456'}
    #
    # list = {'11', '22', '33', '44', '55'}
    # print(add_demo())
    # str_demo()
    # sub = add_demo1(aint=2, bint=3)
    # print(sub)
    # alist = [9, 5, 8, 3, 4, 566, 5]
    # # list_demo()
    # # list_update(alist)
    # pop_demo(alist)
    # print(adict['name'])
    # print(adict['name'])
    # # adict_demo()
    # adict_demo1()






    # list.intqq
    # print(list.intqq)

    pass