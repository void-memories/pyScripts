import time
import os
import urllib.request
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


   

browser = webdriver.Chrome()
driver = webdriver.Chrome(
    executable_path='/Users/voidmemories/Documents/code/py/chromedriver')

x=160
for i in range(900):
    x+=1
    browser.get("http://10.6.3."+str(x))
