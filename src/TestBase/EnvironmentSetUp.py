'''
Created on Jul 4, 2019
 
@author: ganesh.kumar
'''
import os 
import unittest
import datetime
#from selenium import webdriver
from src.TestBase.webdriver import Driver
from src.TestBase import url
from Test.TestUtility.PropertyManager import PropertyManager
from Test.TestUtility.email import email
  
from Test.TestUtility.log import log
 
 
class EnvironmentSetup(unittest.TestCase):
#setUP contains the browser setup attributes
 
    @classmethod
    def setUp(self):
            self.driver = Driver('Chrome')
            self.driver.navigate(url.base_url)
            print("Chrome Environment Set Up")
            print("------------------------------------------------------------------")
            self.driver.instance.set_page_load_timeout(20)
            self.driver.instance.maximize_window()
 
 
#tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDown(self):
        cwd = os.getcwd()
        if (self.driver!=None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.instance.close()
            self.driver.instance.quit()
#             util=email()
#             properties = PropertyManager(cwd+'\config.properties')
#             from_addr = properties.get_property('from_addr')
#             to_addr = properties.get_property('to_addr')
#             file_path = properties.get_property('file_path')
#             util.sendEmail(from_addr,to_addr,cwd+file_path)
#             print("Email sent sucessfully")
             
