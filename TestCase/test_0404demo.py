import time

from selenium.webdriver.common import alert

from Common.Assert import Assertion
from Common.baseui import baseUI


class Testplfahuo:
    def test_plfh(self,driver):
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
        # 点击全选框
        base.click("点击全选框",'(//label[@role="checkbox"]/span/span)[1]')
        # 点击批量操作//input[@placeholder="批量操作"]
        base.click("点击批量操作",'//input[@placeholder="批量操作"]')
        # 点击批量发货//span[text()="批量发货"]
        base.click("点击批量发货",'//span[text()="批量发货"]')
        # 点击确定(//span[contains(text(),"确定")])[1]
        base.click("点击确定",'(//span[contains(text(),"确定")])[1]')

        rows= len(driver.find_elements_by_xpath("//tbody/tr"))

        for i in range(1,rows+1):
            # 点击配送方式//tbody/tr[1]/td[6]//input
            base.click("点击配送方式", '//tbody/tr[{0}]/td[6]//input'.format(i))
            # 选择物流公司(//span[text()="顺丰快递"])[10]
            base.click("选择物流公司", '(//span[text()="顺丰快递"])[10]')
            # 输入物流单号//tbody/tr[1]/td[7]//input
            base.send_keys("输入物流单号",'//tbody/tr[{0}]/td[7]//input'.format(i),'452358767864')
        # 点击确定//span[text()="确定"]
        base.click("点击确定",'//span[text()="确定"]')
        # 点击弹框确定(//span[contains(text(),"确定")])[2]
        base.click("点击弹框确定",'(//span[contains(text(),"确定")])[2]')
        # 获取提示文本框//div[@role="alert"]/p
        text = base.get_text("获取提示文本框", '//div[@role="alert"]/p')
        # 断言
        Assertion.assert_in_text(text,"发货成功")