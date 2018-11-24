from selenium.webdriver.support.wait import WebDriverWait


class Base():
    """
    在Base类中封装常用的公共方法
        1. 查找元素封装
        2. 点击元素封装
        3. 输入方法封装
        *loc = By.XPATH, "//*[contains(@text, 'Fs')]"
    """
    # 传入driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, text):
        el = self.base_find_element(loc)
        el.clear()  # 清空
        el.send_keys(text)  # 输入