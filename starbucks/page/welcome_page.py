from selenium.webdriver.common.by import By

class welcomePage():

    def __init__(self,driver):
        self.driver = driver

    def menu_btn_click(self):
        menu_btn = self.driver.find_element(By.CLASS_NAME,"sb-globalNav__desktopListItem.flex.items-center.sb-globalNav__desktopListItem--active")
        menu_btn.click()