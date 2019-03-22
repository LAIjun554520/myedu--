import json
# 声明一个  全量dict 变量 （字典）

adict = {"name":"laijun","pwd":"554520","1":"数字1"}

# 这是一个字符串  不过是json格式，也是字典格式
adictstr = '{"name":"laijun","pwd":"554520"}'

adictstr1 = '{"name":"laijun","pwd":"554520","1":"数字1"}'

if __name__ == '__main__':
    # 删除name键值对
    # adict.pop("name")
    # print(adict)
    # 打印姓名，打印adict
    # print(adict['name'])
    # print(adict)
    # 字符转换成字典
    # print(type(adictstr))
    # loads = json.loads(adictstr)
    # print(type(loads))
    # # 字典转换成字符
    # dumps = json.dumps(adict)
    # print(type(dumps))
    # 字符转换成字典
    loads = json.loads(adictstr1)
    print(type(adictstr1))
    print(loads)
    # 数字转义成字符,错误编码
    json_dumps = json.dumps(adict)
    print(json_dumps)
    # 把错误编码转成字符
    dumps = json.dumps(loads,ensure_ascii=False)
    print(type(adictstr1))
    print(dumps)
