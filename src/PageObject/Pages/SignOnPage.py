from selenium.webdriver.common.by import By
from Test.TestUtility.log import log
from src.PageObject.Locators import Locator

class SignOn(object):

    
# __init__(self, driver) is like constructor, to initialize the class object or instance of class
#  whenever will call this Class, this will get call and we need to pass the driver
    def __init__(self, driver):
        log.info("ininitilze driver instance")
        self.driver = driver
        #common = GenricFunction(driver)
        
# home page locators defining
        self.userName = driver.instance.find_element(By.XPATH, Locator.signOn_userName)
        self.password = driver.instance.find_element(By.XPATH, Locator.signOn_password)
        self.login = driver.instance.find_element(By.XPATH, Locator.signOn_login)
        self.welcomeText = driver.instance.find_element(By.XPATH, Locator.signOn_txt)
        self.registrationLink = driver.instance.find_element(By.XPATH,Locator.signOn_registerLink)
        
        
    def getSignInPageTitle(self):
            return self.driver.instance.title
     
    def verifyInvalidAccount(self, username, password):
        self.userName.send_keys(username)
        self.password.send_keys(password)
        self.login.click()
        