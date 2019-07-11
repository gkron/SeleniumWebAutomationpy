from selenium.webdriver.common.by import By

from src.PageObject.Locators import Locator


class Confirmation(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.thankYou = driver.instance.find_element(By.XPATH, Locator.thank_you)
        self.UserID = driver.instance.find_element(By.XPATH, Locator.post_user)
        
        
    def getConfirmationPageTitle(self):
            return self.driver.instance.title    