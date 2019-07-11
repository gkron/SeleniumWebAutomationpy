from selenium import webdriver
import os
 
class Driver:
    
     
    def __init__(self,browser):
        cwd = os.getcwd()
        if (browser == 'Chrome'):
            self.instance = webdriver.Chrome(cwd+"\drivers\chromedriver.exe")
        elif (browser == 'FireFox'): 
            self.instance = webdriver.Firefox(executable_path=cwd+"\Demo1\drivers\geckodriver.exe")
           
        else:
            #self.instance = webdriver.Chrome("D:\eclipse-workspace\Demo1\drivers\chromedriver.exe")
            print("no driver")
 
        self.instance.set_page_load_timeout(20)
        self.instance.maximize_window()
 
    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
             
        else:
            raise TypeError("URL must be a string.")