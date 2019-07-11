'''
Created on Jul 4, 2019

@author: ganesh.kumar
'''

from selenium import webdriver

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "D:/eclipse-workspace/UIwebAutomation/ScreenShots"
        self.driver.instance.get_screenshot_as_file(directory+path)