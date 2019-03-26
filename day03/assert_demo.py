

# while  循环
def xunhuan():
    a=0
    while a<10:
        print(a)
        a+=1

#  try except  用来捕捉异常
def zuihou():
    a="8569541635"
    # try用于异常处理,如果出现异常,则执行except内的代码
    try:
        # 断言0是否包含a里
        assert '5'not in a
    #    报错后执行
    except:
        # 打印a里面没有0
        print('a里面有5')
    #     不管是否有异常finally里面的代码都会被执行
    finally:
        print('最后--------')





if __name__ == '__main__':
    zuihou()
    xunhuan()
    pass