import os,sys
sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page_login import PageLogin


class Testlogin():


    #  初始化方法
    def setup_class(self):
        self.login = PageLogin(get_driver())

    # 结束方法
    def teardown_class(self):
        self.login.driver.quit()

    # 测试方法
    def test_login(self, username = "12345678", password = "4846846"):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(password)
        # 确认
        self.login.page_click_login()