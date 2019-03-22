blist=[9,8,5,6,7,4,3,5,1,0]

def list_demo():
    alist=[9,8,5]
    print(alist[0])





def list_update1():
    blist[1]=2
    print(blist[1])
    print(blist)
    # print(blist[3:])


# 列表排序的方法
def orderby_demo():
    print('调用正序排的方法')
    soft_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass

# 正序方法
def soft_demo():
    # 将blist正序排
    blist.sort()
    print(blist)
    pass

# 倒序方法
def reverse_demo():
    # 将blist倒序排
    blist.reverse()
    print(blist)
    pass


if __name__ == '__main__':
    # list_demo()
    # print(blist)
    # alist = [9, 8, 5]
    # print(alist)
    # list_update1()
    # 打印blist的长度：len 长度
    # print(len(blist))
    # .pop 删除最后一位，打印blist去除最后一位
    # print(blist.pop())
    # print(blist)
    # .pop（带参） 删除第4 位，打印blist去除最后4位
    # print(blist.pop(3))
    # print(blist)
    # print(list_update1())
    # 排列的方法
    # orderby_demo()
    blist.append(558)
    print(blist)
    pass
