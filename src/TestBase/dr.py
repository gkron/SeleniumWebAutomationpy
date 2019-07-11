# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 
# class Driver:
#     
# #     def __init__(self,browser):
# #         if (browser == 'Chrome'):
# #             self.instance = webdriver.Chrome("D:\eclipse-workspace\TryQA\drivers\chromedriver.exe")
# #         elif (browser == 'FireFox'): 
# #             self.instance = webdriver.Firefox(executable_path="D:\eclipse-workspace\Demo1\drivers\geckodriver.exe")
# #         else:
# #             self.instance = webdriver.Chrome("D:\eclipse-workspace\Demo1\drivers\chromedriver.exe")
# # 
# #         self.instance.set_page_load_timeout(20)
# #         self.instance.maximize_window()
# 
#     def navigate(self, url):
#         if isinstance(url, str):
#             self.instance.get(url)
#             
#         else:
#             raise TypeError("URL must be a string.")
#         
#     def run_local(self,browser):
#         if (browser == 'Chrome'):
#             self.instance = webdriver.Chrome("D:\eclipse-workspace\TryQA\drivers\chromedriver.exe")
#         elif (browser == 'FireFox'): 
#             self.instance = webdriver.Firefox(executable_path="D:\eclipse-workspace\Demo1\drivers\geckodriver.exe")
#         else:
#             self.instance = webdriver.Chrome("D:\eclipse-workspace\Demo1\drivers\chromedriver.exe")
#             
#     def get_webdriver(self,browser):
#         "Run the test in browser stack browser stack flag is 'Y'"
#         USERNAME = "ganesh476" #We fetch values from a conf file in our framework we use on our clients
#         PASSWORD = "JrTbqPnBHEdJ1hfGiZVW"
#         if browser.lower() == 'firefox':
#             desired_capabilities = DesiredCapabilities.FIREFOX
#         if browser.lower() == 'chrome':
#             desired_capabilities = DesiredCapabilities.CHROME
#         desired_capabilities['os'] = 'Windows'
#         desired_capabilities['os_version'] = '7'
#         desired_capabilities['browser_version'] = '63'
#      
#         return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub'%(USERNAME,PASSWORD),
#                                 desired_capabilities=desired_capabilities)   
#         
#         