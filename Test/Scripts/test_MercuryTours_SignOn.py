import unittest
#from time import sleep

#from PageObject.Pages.SignOnPage import SignOn
from src.PageObject.Pages.SignOnPage import SignOn
from src.TestBase.EnvironmentSetUp import EnvironmentSetup
from src.PageObject.Pages.HomePage import Home
from src.PageObject.Pages.ConfirmationPage import Confirmation
#from Test.TestUtility.ScreenShot import SS
#from Test.TestUtility.log import log


class MercuryTours_SignOn(EnvironmentSetup):

    def test_verifySignInPageTitle(self):
        driver = self.driver
        home = Home(driver)
        home.clickSignOn()
        signon=SignOn(driver)
        actual=signon.getSignInPageTitle()
        print(actual)
        assert actual == "Sign-on: Mercury Tours"
        

    def test_verifyInvalidUserName(self):
        driver = self.driver
        home = Home(driver)
        home.sign_on.click()
        signon=SignOn(driver)
        signon.verifyInvalidAccount("ron", "qa")
        actual=signon.getSignInPageTitle()
        assert actual == "Sign-on: Mercury Tours"
    
    def test_verifyValidLoginPage(self):
        driver = self.driver
        home = Home(driver)
        home.sign_on.click()
        signon=SignOn(driver)
        signon.verifyInvalidAccount("gkron184@gmail.com", "123456")
        post = Confirmation(driver)
        actual=post.getConfirmationPageTitle()
        print(actual)
        assert actual == "Find a Flight: Mercury Tours:"
#     def test_SignOnPage(self):
#         driver = self.driver
#         home = Home(driver)
#         home.sign_on.click()
#         sleep(2)
#         if driver.instance.title == "Sign-on: Mercury Tours":
#             print("Sign On page loaded successfully")
# 
#         else:
#             print("SignOn page failed to load")
# 
#         login = SignOn(driver)
#         try:
#             print(login.welcomeText.get_attribute("innerText"))
#             if login.registrationLink.text.find("registration"):
#                 print("Registration link :"+login.registrationLink.get_attribute("href"))
# 
#             print("Provide invalid username")
#             login.userName.send_keys("Invalid")
#             print("Provide invalid password")
#             login.password.send_keys("Invalid")
#             sleep(2)
#             login.login.click()
#             sleep(2)
#             if driver.instance.title == "Sign-on: Mercury Tours":
#                 print("Invalid Credentials Provided")
#         except Exception as e:
#             print("Exception occurred "+e)




if __name__ == '__main__':
    unittest.main()
