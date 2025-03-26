from selenium_1.base_selenium_starter import baseSeleniumStarter
from starbucks.page.welcome_page import welcomePage


def test_menu_btn_works_test():
    base = baseSeleniumStarter()
    driver = base.selenium_init()
    welcome_page = welcomePage(driver)
    driver.get("https://www.starbucks.com/menu")
    welcome_page.menu_btn_click()

    assert driver.current_url == "https://www.starbucks.com/menu" , "The new page didn't open"

    base.selenium_end(driver)
