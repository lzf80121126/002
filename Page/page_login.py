from selenium.webdriver.common.by import By

from Base.base import Base

class PageLogin(Base):
    """
    一个页面封装成一个对象(新建一个class)
    对象页面内写需要操作的步骤,每一个步骤单独封装一个方法
    """

    loc_un = (By.ID, "com.vcooline.aike:id/etxt_username")
    loc_pwd = By.ID, "com.vcooline.aike:id/etxt_pwd"
    loc_login = By.ID, "com.vcooline.aike:id/btn_login"

    def page_input_username(self, text):
        """
        调用的base类封装输入方法,因为集成直接通过self调用
        :param loc:
        :param text:
        :return:
        """
        self.base_find_element(self.loc_un,text)

    def page_input_password(self, text):
        self.base_find_element(self.loc_pwd, text)

    def page_click_login(self):
        self.base_click_element(self.loc_login)

