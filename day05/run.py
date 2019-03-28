import pytest

if __name__ == '__main__':
    pass
    # 调用测试框架 pytest  --alluredir : 指定allure 的目录地址, ../Report/xml
    pytest.main(['-s', '-q', '--alluredir','../Report/xml/''.'])

    # allure generate. / Report / xml / -o. / Report / html / --clean