#NOTE: This is highly simplified code to make this post illustrative
#We do not use this code at clients
#We use Driver_Factory to return apporpriate drivers within our framework
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
def get_webdriver(browser,browser_version,platform,os_version):
    "Run the test in browser stack browser stack flag is 'Y'"
    USERNAME = "ganesh476" #We fetch values from a conf file in our framework we use on our clients
    PASSWORD = "JrTbqPnBHEdJ1hfGiZVW"
    if browser.lower() == 'firefox':
        desired_capabilities = DesiredCapabilities.FIREFOX
    if browser.lower() == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['os'] = platform
    desired_capabilities['os_version'] = os_version
    desired_capabilities['browser_version'] = browser_version
 
    return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub'%(USERNAME,PASSWORD),
                            desired_capabilities=desired_capabilities)