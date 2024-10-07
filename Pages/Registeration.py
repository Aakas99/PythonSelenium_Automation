#import pytest
from selenium.webdriver.common.by import By

#@pytest.mark.usefixtures("setup")
class Registerationpage:
    def __init__(self, driver):
        self.driver = driver

    Male = (By.XPATH, "(//input[@name='Gender'])[1]")
    Female = (By.XPATH, "(//input[@name='Gender'])[2]")
    Firstname = (By.XPATH, "//input[@id='FirstName']")
    Lastname = (By.XPATH, "//input[@id='LastName']")
    Email = (By.XPATH, "//input[@id='Email']")
    Pass = (By.XPATH, "//input[@id='Password']")
    ConfirmPass = (By.XPATH, "//input[@id='ConfirmPassword']")
    Register = (By.XPATH, "//input[@value='Register']")
    Continue = (By.XPATH,"//input[@value='Continue']")
    def GenderSelection(self):
        return self.driver.find_element(*Registerationpage.Male)

    def Fname(self):
        return self.driver.find_element(*Registerationpage.Firstname)

    def Lname(self):
        return self.driver.find_element(*Registerationpage.Lastname)

    def Email_ID(self):
        return self.driver.find_element(*Registerationpage.Email)

    def Password(self):
        return self.driver.find_element(*Registerationpage.Pass)
    
    def Confirmpassword(self):
        return self.driver.find_element(*Registerationpage.ConfirmPass)
    
    def Registerion (self):
        return self.driver.find_element(*Registerationpage.Register)
    
    def Continue_button (self):
        return self.driver.find_element(*Registerationpage.Continue)
    