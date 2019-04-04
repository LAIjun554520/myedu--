import time

from selenium.webdriver.common import alert

from Common.Assert import Assertion
from Common.baseui import baseUI


class Testfahuo:
    def test_fh(self,driver):
        base = baseUI(driver)
#         打开网址

        driver.get("http://192.168.60.132/#/login")
#         输入用户名
        base.send_keys("输入用户名", "//input[@name='username']", 'admin')
#         输入密码
        base.send_keys("输入密码","//input[@name='password']", '123456')
#         点击登录

        base.click("登录","//span[contains(text(),'登录')]")
        # 点击订单
        base.click("订单",'//span[contains(text(),"订单")]')
        # 订单列表
        base.click("订单列表",'//span[contains(text(),"订单列表")]')
        # 订单状态
        base.click("订单状态",'//label[contains(text(),"订单状态：")]/following-sibling::div//input')
        # 待发货
        base.click("待发货",'//span[contains(text(),"待发货")]')
        # 查询搜索
        base.click("查询搜索",'//span[contains(text(),"查询搜索")]')
        time.sleep(2)
        # 记录第一条编号//tbody/tr[1]/td[2]/div
        num = base.get_text("记录第一条编号", '//tbody/tr[1]/td[2]/div')
        order_num = base.get_text("获取订单编号", '//tbody/tr[1]/td[3]/div')

        # 发货    //tbody/tr[1]/td[10]/div/button[3]
        base.click("发货",'//tbody/tr[1]/td[10]/div/button[3]')
        # 选择物流公司
        base.click("物流公司",'(//td)[6]//input')
        # 选择快递
        base.click("快递",'//span[contains(text(),"顺丰快递")]')
        # 物流单号
        base.send_keys("物流单号",'(//td)[7]//input',"987562435")
        # 点击确定//span[text()="确定"]
        base.click("确定",'//span[text()="确定"]')
        time.sleep(2)
        # 弹框确定
        # base.click("点击确定",'(//span[contains(text(),"确定")]/parent::button//span)[2]')
        base.click("点击确定", '(//span[contains(text(),"确定")])[2]')
        # 获取提示框文本//div[@role="alert"]/p
        text = base.get_text("获取提示框文本","//div[@role='alert']/p")


        # 断言
        Assertion.assert_in_text(text, '发货成功')
        # 订单状态
        base.click("订单状态", '//label[contains(text(),"订单状态：")]/following-sibling::div//input')
        # 待发货
        base.click("已发货", '//span[contains(text(),"已发货")]')
        # 输入订单编号//input[@placeholder="订单编号"]
        base.send_keys('输入订单编号','//input[@placeholder="订单编号"]',order_num)
        # 查询搜索
        base.click("查询搜索", '//span[contains(text(),"查询搜索")]')
        #定位到刚才发货的订单
        time.sleep(1)
        #通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        #存放是否能找到编号 找到true  未找到 false
        b = False
        #遍历上边的list
        for n in nums:
            #n.text取出元素的可视文本
            print(n.text)
            #判断可视文本是否与发货订单的编号相同
            if n.text ==num:
                #如果相同，就讲true赋值给b
                b = True
        #断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)




