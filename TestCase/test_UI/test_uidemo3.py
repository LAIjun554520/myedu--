import time

from Common.baseui import baseUI



class TestFistUIDemo:
    def test_testdemo1(self, driver):
        base = baseUI(driver)
        #登录网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys('输入用户名','//input[@name="username"]','admin')
        # 输入密码
        base.send_keys('输入密码','//input[@name="password"]','123456')
        # 点击登录
        base.click("登录",'//span[contains(text(),"登录")]')
        time.sleep(2)
        #点击商品
        base.click("商品",'//span[contains(text(),"商品")]')
        time.sleep(2)
        # 点击添加商品
        base.click("添加商品",'//span[contains(text(),"添加商品")]')
        time.sleep(2)
        # 点击商品分类
        base.click("商品分类",'(//label[contains(text(),"商品分类：")]/following-sibling::div//span)[4]')
        time.sleep(2)
        # 点击商品分类家用电器下拉框
        base.click("家用电器",'//li[contains(text(),"家用电器")]')
        # 点击二级洗衣机下拉框
        base.click("洗衣机",'//li[contains(text(),"洗衣机")]')
        # 点击商品名称
        base.send_keys("商品名称",'//label[contains(text(),"商品名称：")]/following-sibling::div//input',"长虹洗衣机")
        # 点击副标题
        base.send_keys("副标题",'//label[contains(text(),"副标题：")]/following-sibling::div//input',"家用洗衣机")
        # 点击商品品牌
        base.click("商品品牌",'//label[contains(text(),"商品品牌：")]/following-sibling::div/div')
        # 点击格力
        base.click("格力",'//span[contains(text(),"格力")]')
        # 商品介绍
        base.send_keys("商品介绍",'//label[contains(text(),"商品介绍：")]/following-sibling::div//textarea',"洗衣机")
        # 商品货号
        base.send_keys("商品货号",'//label[contains(text(),"商品货号：")]/following-sibling::div//input',"789562")
        # 商品售价
        base.send_keys("商品售价",'//label[contains(text(),"商品售价：")]/following-sibling::div//input',"789562")
        # 市场价
        base.send_keys("市场价",'//label[contains(text(),"市场价：")]/following-sibling::div//input',"999999")
        # 商品库存
        base.send_keys("商品库存",'//label[contains(text(),"商品库存：")]/following-sibling::div//input',"100000")
        # 下拉滚动条
        base.scroll_screen("下拉滚动条")
        # 计量单位
        base.send_keys("计量单位",'//label[contains(text(),"计量单位：")]/following-sibling::div//input',"***")
        # 商品重量
        base.send_keys("商品重量",'//label[contains(text(),"商品重量：")]/following-sibling::div//input',"99999")
        # 排序
        base.send_keys("排序",'//label[contains(text(),"排序")]/following-sibling::div//input',"2")
        # 点击下一步
        base.click("下一步",'//span[contains(text(),"下一步，填写商品促销")]')
        # 赠送积分
        base.send_keys("赠送积分",'//label[contains(text(),"赠送积分：")]/following-sibling::div//input','100')
        # 赠送成长值
        base.send_keys("赠送成长值",'//label[contains(text(),"赠送成长值：")]/following-sibling::div//input','50')
        # 积分购买限制
        base.send_keys("积分购买限制",'//label[contains(text(),"积分购买限制：")]/following-sibling::div//input','200')
        # 预告商品
        base.click("预告商品",'//label[contains(text(),"预告商品：")]/following-sibling::div//span')
        # 商品上架
        base.click("商品上架",'//label[contains(text(),"商品上架：")]/following-sibling::div//span')
        # 商品推荐
        base.click("商品推荐",'(//label[contains(text(),"商品推荐：")]/following-sibling::div//span)[4]')
        # 服务保证
        base.click("服务保证",'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[2]')
        base.click("服务保证",'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[5]')
        base.click("服务保证",'(//label[contains(text(),"服务保证：")]/following-sibling::div//span)[8]')
        # 详细页标题
        base.send_keys("详细页标题",'//label[contains(text(),"详细页标题：")]/following-sibling::div//input','bbbbb')
        # 详细页描述
        base.send_keys("详细页描述",'//label[contains(text(),"详细页描述：")]/following-sibling::div//input','101010101')
        # 商品关键字
        base.send_keys("商品关键字",'//label[contains(text(),"商品关键字：")]/following-sibling::div//input','bbbbb')
        # 商品备注
        base.send_keys("商品备注",'//label[contains(text(),"商品备注：")]/following-sibling::div//textarea','10101010')
        # 选择优惠方式
        base.click("选择优惠方式",'(//label[contains(text(),"选择优惠方式：")]/following-sibling::div//span)[2]')
        # 特惠促销
        #     开始时间
        base.send_keys("开始时间",'//div[contains(text(),"开始时间：")]/div/input','2019-04-02 16:25:01')
        # 结束时间
        base.send_keys("结束时间",'//div[contains(text(),"结束时间：")]/div/input','2019-04-10 16:32:01')
        # 促销价格
        base.send_keys("促销价格",'//div[contains(text(),"促销价格：")]/div/input','9999')
        # 下一步，填写商品属性
        base.click("下一步",'//span[contains(text(),"下一步，填写商品属性")]')
        # 下一步，选择商品关联
        base.click("下一步",'//span[contains(text(),"下一步，选择商品关联")]')
        # 完成，提交商品
        base.click("完成",'//span[contains(text(),"完成，提交商品")]')


