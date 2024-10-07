from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Pages.HomePage import Homepage
from Pages.Registeration import Registerationpage
from TestData.RegistrationData import RegistrationData
from Utilities.BaseClass import BaseClass

class TestFunctionality_testcase(BaseClass):
    

    def test_register_logout(self,getData):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        Register = Registerationpage(self.driver)
        homepage.new_register().click()
        log.info("Clicking on register link")
        
        Register.GenderSelection().click()
        log.info("Choosing gender of user")
        Register.Fname().send_keys(getData["firstname"])
        log.info("Entering first name")
        Register.Lname().send_keys(getData["lastname"])
        log.info("Entering last name")
        Register.Email_ID().send_keys(getData["EmailID"])
        log.info("Entering Email id")
        Register.Password().send_keys(getData["Password"])
        log.info("Creating new password")
        Register.Confirmpassword().send_keys(getData["Password"])
        log.info("Confirming new password")
        #Register.Registerion().click()
        #Register.Continue_button().click()
        #homepage = Homepage(self.driver)
        #
        #homepage.logout().click()
    

        

          
               

        
    
    
    

       
    
    @pytest.fixture(params=RegistrationData.test_HomePage_data)
    def getData(self, request):
        return request.param
        
