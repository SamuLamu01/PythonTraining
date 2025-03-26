from selenium.webdriver.common.by import By

class findAStore():

    def __init__(self,driver):
        self.driver = driver

    def find_a_store_click(self):
        find_a_store = self.driver.find_element(By.CLASS_NAME,"sb-textLink.text-noUnderline.text-semibold.sb-findAStorePin.inline-block.pr3.pr2")
        find_a_store.click()

