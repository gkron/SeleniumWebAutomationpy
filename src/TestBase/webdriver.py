from selenium import webdriver
 
class Driver:
     
    def __init__(self,browser):
        if (browser == 'Chrome'):
            self.instance = webdriver.Chrome("D:\eclipse-workspace\TryQA\drivers\chromedriver.exe")
        elif (browser == 'FireFox'): 
            self.instance = webdriver.Firefox(executable_path="D:\eclipse-workspace\Demo1\drivers\geckodriver.exe")
        else:
            self.instance = webdriver.Chrome("D:\eclipse-workspace\Demo1\drivers\chromedriver.exe")
 
        self.instance.set_page_load_timeout(20)
        self.instance.maximize_window()
 
    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
             
        else:
            raise TypeError("URL must be a string.")