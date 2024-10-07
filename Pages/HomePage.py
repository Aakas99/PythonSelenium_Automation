#import pytest
from selenium.webdriver.common.by import By

#@pytest.mark.usefixtures("setup")
class Homepage:
    def __init__(self, driver):
        self.driver = driver

    newRegister = (By.XPATH, "//a[text()='Register']")
    log_out = (By.XPATH, "//a[text()='Log out']")
    def new_register(self):
       return self.driver.find_element(*Homepage.newRegister)
    def logout(self):
       return self.driver.find_element(*Homepage.log_out)
