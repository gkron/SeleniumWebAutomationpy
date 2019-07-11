import unittest
from time import sleep
#from PageObject.Pages.SignOnPage import SignOn
#from src.PageObject.Pages.SignOnPage import SignOn

from src.TestBase.EnvironmentSetUp import EnvironmentSetup
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.RegistrationPage import Register
from src.PageObject.Pages.ConfirmationPage import Confirmation
#from wheel.signatures import assertTrue


class MercuryTours_Registration(EnvironmentSetup):
    
    
    def test_RegistrationFlow(self):
        driver = self.driver
        home = Home(driver)
        if home.getRegister().is_displayed():
            print("Register Link displaying")
            home.getRegister().click()
        else:
            print("Rigister link is not displayed")
        reg= Register(driver)
        if reg.getRegis_txt().is_displayed():
            print(reg.regis_txt.text)
        else:
            print("Registration page not loaded")
        try:
            reg.setFirstName("ganesh")
            reg.setLastName("kumar")
            reg.setPhone("9999135778")
            reg.setEmail("gkron184@gmail.com")
            reg.setCountry("INDIA")
            reg.setUserName("gkron184@gmail.com")
            reg.setPassword(123456)
            reg.setConfirmPassword(123456)
            sleep(2)
            reg.submitRegistration()
            sleep(4)
        except Exception as e:
            print("Exception occurred "+e)    
            
    #calling Post Registration check
        post = Confirmation(driver)
        print(post.thankYou.text)
        if (post.UserID.text).find("gkron184@gmail.com"):
            print("Registration Process Successful")
        else:
            print("User Failed to register properly")        
            
            
if __name__ == '__main__':
    unittest.main()            