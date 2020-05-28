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
browser.get('http://kletecheresults.contineo.in/')


cap = input()
f=open("final.txt","a")


for i in range(10, 99):
    f1=f2=f3=0
    u = browser.find_element_by_id("usn")
    c = browser.find_element_by_id("osolCatchaTxt0")
    # new="01fe17bcs"+i
    u.send_keys(f"01fe17bcs0{i}")
    c.send_keys(cap, Keys.TAB, Keys.TAB, Keys.ENTER)

    iter = browser.find_elements_by_class_name("headingdateWhite")

    for j in iter:
        xxx=j.get_attribute("textContent")
        print(xxx)
        f.write(xxx)
        f.write('\n')

    iter2=browser.find_elements_by_class_name("box")

    for j in iter2:
        xxx=j.get_attribute("textContent")
        print(xxx)
        f.write(xxx)
        f.write('\n')

    

    images = browser.find_elements_by_tag_name("img")
    for image in images:
        src = image.get_attribute("src")
        urllib.request.urlretrieve(src, f"{image}.jpg")
#    browser.find_element_by_link_text('Print Provisional Grade Card').click()
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    browser.back()
f.close()
