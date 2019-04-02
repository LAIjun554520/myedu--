import selenium
from selenium import webdriver
import time
import os

from Common.Assert import Assertions
# from Common.baseuii import send_keys, click_demo


class TestFistUIDemo:
    def test_testdemo1(self,driver):
        # # 打开浏览器
        # # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # print(driver_path)
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)
        driver.get("http://192.168.60.132/#/login")
        # 先输入用户名

        send_keys(driver,'//input[@name="username"]','admin')

        # username = driver.find_element_by_xpath('//input[@name="username"]')
        # username.clear()
        # username.send_keys('admin')
        # time.sleep(2)


        # 在输入密码

        send_keys(driver,'//input[@name="password"]','123456')

        # password = driver.find_element_by_xpath('//input[@name="password"]')
        # password.clear()
        # password.send_keys('123456')
        # time.sleep(2)

        # 最后点击登录
        click_demo(driver,"//span[contains(text(),'登录')]")

        # 点击商品

        click_demo(driver,'//span[contains(text(),"商品")]')

        # shangping = driver.find_element_by_xpath('//span[contains(text(),"商品")]')
        # shangping.click()
        # time.sleep(2)

        # 点击添加商品

        click_demo(driver,'//span[contains(text(),"添加商品")]')

        # tianjia = driver.find_element_by_xpath('//span[contains(text(),"添加商品")]')
        # tianjia.click()
        # time.sleep(2)


        # 点击商品分类

        click_demo(driver,'(//label[contains(text(),"商品分类：")]/following-sibling::div//span)[4]')

        # dianjishangpingfenlei = driver.find_element_by_xpath('(//label[contains(text(),"商品分类：")]/following-sibling::div//span)[4]')
        # dianjishangpingfenlei.click()
        # time.sleep(2)

        # 点击商品分类家用电器下拉框

        click_demo(driver,'//li[contains(text(),"家用电器")]')

        # jiayongdianqi = driver.find_element_by_xpath('//li[contains(text(),"家用电器")]')
        # jiayongdianqi.click()
        # time.sleep(2)

        # 点击二级洗衣机下拉框

        click_demo(driver,'//li[contains(text(),"洗衣机")]')

        # xiyiji = driver.find_element_by_xpath('//li[contains(text(),"洗衣机")]')
        # xiyiji.click()
        # time.sleep(2)

        # 点击商品名称

        send_keys(driver,'//label[contains(text(),"商品名称：")]/following-sibling::div//input',"长虹洗衣机")

        # shangpinmingcheng = driver.find_element_by_xpath('//label[contains(text(),"商品名称：")]/following-sibling::div//input')
        # shangpinmingcheng.clear()
        # shangpinmingcheng.send_keys("长虹洗衣机")
        # time.sleep(2)

        # 点击副标题

        send_keys(driver,'//label[contains(text(),"副标题：")]/following-sibling::div//input',"家用洗衣机")

        # fubiaoti = driver.find_element_by_xpath('//label[contains(text(),"副标题：")]/following-sibling::div//input')
        # fubiaoti.clear()
        # fubiaoti.send_keys("家用洗衣机")
        # time.sleep(2)

        # 点击商品品牌

        click_demo(driver,'//label[contains(text(),"商品品牌：")]/following-sibling::div/div')

        # pingpai = driver.find_element_by_xpath('//label[contains(text(),"商品品牌：")]/following-sibling::div/div')
        # pingpai.click()
        # time.sleep(2)

        # 点击格力

        click_demo(driver,'//span[contains(text(),"格力")]')

        # geli = driver.find_element_by_xpath('//span[contains(text(),"格力")]')
        # geli.click()
        # time.sleep(2)

        # 商品介绍

        send_keys(driver,'//label[contains(text(),"商品介绍：")]/following-sibling::div//textarea',"洗衣机")

        # shangpinjieshao = driver.find_element_by_xpath('//label[contains(text(),"商品介绍：")]/following-sibling::div//textarea')
        # shangpinjieshao.clear()
        # shangpinjieshao.send_keys("洗衣机")
        # time.sleep(2)

        # 商品货号

        send_keys(driver,'//label[contains(text(),"商品货号：")]/following-sibling::div//input',"789562")

        # huohao = driver.find_element_by_xpath('//label[contains(text(),"商品货号：")]/following-sibling::div//input')
        # huohao.clear()
        # huohao.send_keys("789562")
        # time.sleep(2)

        # 商品售价

        send_keys(driver,'//label[contains(text(),"商品售价：")]/following-sibling::div//input',"789562")

        # shoujia = driver.find_element_by_xpath('//label[contains(text(),"商品售价：")]/following-sibling::div//input')
        # shoujia.clear()
        # shoujia.send_keys("789562")
        # time.sleep(2)

        # 市场价

        send_keys(driver,'//label[contains(text(),"市场价：")]/following-sibling::div//input',"999999")

        # shichangjia = driver.find_element_by_xpath('//label[contains(text(),"市场价：")]/following-sibling::div//input')
        # shichangjia.clear()
        # shichangjia.send_keys("999999")
        # time.sleep(2)

        # 商品库存

        send_keys(driver,'//label[contains(text(),"商品库存：")]/following-sibling::div//input',"100000")

        # kucun = driver.find_element_by_xpath('//label[contains(text(),"商品库存：")]/following-sibling::div//input')
        # kucun.clear()
        # kucun.send_keys("100000")
        # time.sleep(2)

        # 下拉滚动条

        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

        # 计量单位

        send_keys(driver,'//label[contains(text(),"计量单位：")]/following-sibling::div//input',"***")

        # danwei= driver.find_element_by_xpath('//label[contains(text(),"计量单位：")]/following-sibling::div//input')
        # danwei.clear()
        # danwei.send_keys("***")
        # time.sleep(2)

        # 商品重量

        send_keys(driver,'//label[contains(text(),"商品重量：")]/following-sibling::div//input',"99999")

        # zhongliang= driver.find_element_by_xpath('//label[contains(text(),"商品重量：")]/following-sibling::div//input')
        # zhongliang.clear()
        # zhongliang.send_keys("99999")
        # time.sleep(2)

        # 排序

        send_keys(driver,'//label[contains(text(),"排序")]/following-sibling::div//input',"2")

        # paixu= driver.find_element_by_xpath('//label[contains(text(),"排序")]/following-sibling::div//input')
        # paixu.clear()
        # paixu.send_keys("2")
        # time.sleep(2)

        # 点击下一步

        click_demo(driver,'//span[contains(text(),"下一步，填写商品促销")]')

        # xiayibu = driver.find_element_by_xpath('//span[contains(text(),"下一步，填写商品促销")]')
        # xiayibu.click()
        # time.sleep(2)

        # 赠送积分

        send_keys(driver,'//label[contains(text(),"赠送积分：")]/following-sibling::div//input','100')

        # 赠送成长值

        send_keys(driver,'//label[contains(text(),"赠送成长值：")]/following-sibling::div//input','50')

        # 积分购买限制

        send_keys(driver,'//label[contains(text(),"积分购买限制：")]/following-sibling::div//input','200')

        # 预告商品

        click_demo(driver,'//label[contains(text(),"预告商品：")]/following-sibling::div//span')

        # 商品上架

        click_demo(driver,'//label[contains(text(),"商品上架：")]/following-sibling::div//span')

        # 商品推荐

        click_demo(driver,'(//label[contains(text(),"商品推荐：")]/following-sibling::div//span)[4]')

        # 服务保证

        click_demo(driver,'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[2]')
        click_demo(driver,'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[5]')
        click_demo(driver,'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[8]')

        # 详细页标题

        send_keys(driver,'//label[contains(text(),"详细页标题：")]/following-sibling::div//input','bbbbb')

        # 详细页描述

        send_keys(driver,'//label[contains(text(),"详细页描述：")]/following-sibling::div//input','101010101')

        # 商品关键字

        send_keys(driver,'//label[contains(text(),"商品关键字：")]/following-sibling::div//input','bbbbb')

        # 商品备注

        send_keys(driver,'//label[contains(text(),"商品备注：")]/following-sibling::div//textarea','10101010')

        # 选择优惠方式

        click_demo(driver,'(//label[contains(text(),"选择优惠方式：")]/following-sibling::div//span)[2]')


        # 特惠促销
        #     开始时间
        send_keys(driver,'//div[contains(text(),"开始时间：")]/div/input','2019-04-02 16:25:01')

        # 结束时间

        send_keys(driver,'//div[contains(text(),"结束时间：")]/div/input','2019-04-10 16:32:01')

        # 促销价格

        send_keys(driver,'//div[contains(text(),"促销价格：")]/div/input','9999')



        # 下一步，填写商品属性

        click_demo(driver,'//span[contains(text(),"下一步，填写商品属性")]')

        # xiayibu1 = driver.find_element_by_xpath('//span[contains(text(),"下一步，填写商品属性")]')
        # xiayibu1.click()
        # time.sleep(2)

        # 下一步，选择商品关联

        click_demo(driver,'//span[contains(text(),"下一步，选择商品关联")]')

        # xiayibu2 = driver.find_element_by_xpath('//span[contains(text(),"下一步，选择商品关联")]')
        # xiayibu2.click()
        # time.sleep(2)

        # 完成，提交商品

        click_demo(driver,'//span[contains(text(),"完成，提交商品")]')

        # wancheng = driver.find_element_by_xpath('//span[contains(text(),"完成，提交商品")]')
        # wancheng.click()
        # time.sleep(2)

        # 确定

        click_demo(driver,'(//span[contains(text(),"确定")])[3]')

        # queding = driver.find_element_by_xpath('//span[contains(text(),"确定")]')
        # queding.click()
        # time.sleep(2)






        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '填写商品信息')
        # driver.quit()

