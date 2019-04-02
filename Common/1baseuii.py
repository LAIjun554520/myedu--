import time


def send_keys(driver,xpath,text):
    username = driver.find_element_by_xpath(xpath)
    username.clear()
    username.send_keys(text)
    time.sleep(1)


def click_demo(driver,xpath):
    login = driver.find_element_by_xpath(xpath)
    login.click()
    time.sleep(1)