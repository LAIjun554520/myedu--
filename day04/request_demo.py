# 发请求的
import requests


if __name__ == '__main__':
    # 登录
    # 声明login_data变量名用来存登录请求数据
    login_data = {"username":"admin","password":"123456"}
    # = 号后面就是发起一个请求,使用requests.post方法,入参,有两个url:请求地址,json:请求数据
    login_response = requests.post(url='http://192.168.60.132:8080/admin/login', json=login_data)
    # print(type(login_response))
    # .text  就是获取响应正文(str类型)
    login_response_text = login_response.text
    print(login_response_text)

    # 获取响应正文(字典类型)响应正文必须是json格式
    login_response_json  = login_response.json()
    # print(type(login_response_json))
    # 取出响应正文中的message 的值
    # print(login_response_json['message'])

    # print(login_response_json)
    # 取tokenHead和token
    response_json_data_ = login_response_json['data']
    token_head_ = response_json_data_['tokenHead']
    token_ = response_json_data_['token']
    # 封装token
    head = {'Authorization':token_head_+token_}
    # info请求
    requests_get = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(requests_get.json())
    #订单列表
    # get 请求 : url?k=v& k2=v2
    getorder_param={"pageNum":"1","pageSize":"10"}
    get_order_resp = requests.get(url='http://192.168.60.132:8080/order/list', params=getorder_param, headers=head)
    print(get_order_resp.json())
    order_json = get_order_resp.json()
    order_json_data_ = order_json['data']
    order_json_data__list_ = order_json_data_['list']
    print(order_json_data__list_[0])
    for i in order_json_data__list_:
        print(i)


    # 删除订单

    response_del = requests.post(url='http://192.168.60.132:8080/order/delete?ids=44', headers=head)
    print(response_del.json())

    # 订单发货
    delivery_data=[{"deliveryCompany":"顺丰快递","deliverySn":"5896545","orderId":"61"}]
    r = requests.post(url='http://192.168.60.132:8080/order/update/delivery', headers=head,json=delivery_data)
    print(r.json())

    pass
