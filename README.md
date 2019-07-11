# SeleniumWebAutomationpy
A Pythonic Selenium test automation framework
You can use this test automation framework to write:

Selenium and Python automation scripts to test web applications
This framework is written in Python and is based on the Page Object Model - a design pattern that makes it easy to maintain and develop robust tests. 

Setup
The setup for our open-sourced Python test automation framework is fairly simple. Don't get fooled by the length of this section. We have documented the setup instructions in detail so even beginners can get started.

The setup has four parts:

Prerequisites
Setup for GUI/Selenium automation

1. Prerequisites

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) If you do not have it already, get pip (NOTE: Most recent Python distributions come with pip)

d) pip install -r requirements.txt to install dependencies

2. Setup for GUI/Selenium automation

a) Get setup with your browser driver. If you don't know how to, please try:

For Chrome

For Firefox

#Note: Check Firefox version & Selenium version compatibility before downloading geckodriver.

If your setup goes well, you should be to run a simple test with this command:

e.g hit pytest and all test case will get executed

#Rerun Failed:
pytest --reruns 2 

#Parallel execution
pytest -n <numberofbrowser> e.g 3

#Report
pytest --html= "dir localtion" + report.html

