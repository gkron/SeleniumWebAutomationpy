#Contents of conftest.py
import pytest
import os

 
 
@pytest.fixture
def browser(request):
    print("pytest fixture for browser")
    return request.config.getoption("-B")
 
 
@pytest.fixture
def browser_version(request):
    print("pytest fixture for browser version")
    return request.config.getoption("-V") 
  
  
@pytest.fixture
def platform(request):
    print("pytest fixture for platform")
    return request.config.getoption("-P") 
  
  
@pytest.fixture
def os_version(request):
    print("pytest fixture for os version")
    return request.config.getoption("-O") 
 
 
def pytest_addoption(parser):
    parser.addoption("-B","--browser",
                      dest="browser",
                      default="firefox",
                      help="Browser. Valid options are firefox, ie and chrome") 
    parser.addoption("-M","--browserstack_flag",
                      dest="browserstack_flag",
                      default="N",
                      help="Run the test in Browserstack: Y or N")
    parser.addoption("-V","--ver",
                      dest="browser_version",
                      help="The version of the browser: a whole number",
                      default=45)
    parser.addoption("-P","--platform",
                      dest="platform",
                      help="The operating system: Windows 7, Linux",
                      default="Windows")
    parser.addoption("-O","--os_version",
                      dest="os_version",
                      help="The operating system: xp, 7",
                      default="7")