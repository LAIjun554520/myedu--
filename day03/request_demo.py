

import requests

def login_demo():
    # 封装请求参数
    data = {"username": "admin", "password": "123456"}
    # 发送请求 带上两个参数 url 和请求正文 json
    response = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    # .把响应报文用str格式显示
    text_body = response.text
    print(type(text_body))
    print(text_body)
    # 把响应报文用dict格式显示
    json_body = response.json()
    print(type(json_body))
    print(json_body)

    # assert 200==response.status_code
    # assert '成功' in json_body['message']
    # assert 200== json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head+' '+token_}

    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    info_json = get_info.json()
    print(get_info)
    # print(get_info.text)
    assert 200==get_info.status_code
    assert 200==info_json['code']
    assert '成功'in info_json['message']


    # requests.get('http://192.168.60.132:8080/order/list?pageNum=1&pageSize=10',headers=head)
    param = {'pageNum':1,'pageSize':3}
    get = requests.get('http://192.168.60.132:8080/order/list', params=param, headers=head)
    print(get.text)
    json=get.json()
    json_data_ = json['data']
    list_ = json_data_['list']
    for i in list_:
        print(i)



    data=[
          {
            "deliveryCompany": "顺丰",
            "deliverySn": "985654658",
            "orderId": 40
          }
]

    r = requests.post(url='http://192.168.60.132:8080/order/update/delivery', json=data, headers=head)
    r_text = r.text
    print(type(r_text))
    print(r_text)


    # requests.post(url=)


if __name__ == '__main__':
    login_demo()

    pass