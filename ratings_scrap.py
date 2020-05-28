import time
import os
import urllib.request
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


compi_name='FEB20A'

browser = webdriver.Chrome()
driver = webdriver.Chrome(
    executable_path='/Users/voidmemories/Documents/code/py/chromedriver')

page_no=1

f=open("ratings.txt","a")
while page_no<5:

    try:
        nav_to='https://www.codechef.com/rankings/'+compi_name+'?order=asc&page='+str(page_no)+'&sortBy=rank'
        browser.get(nav_to)
        iter = browser.find_elements_by_class_name("num")
        for i in iter:
            if (i.get_attribute("cellIndex"))=='2':
                f.write(i.get_attribute("innerText"))
                f.write('\n')
    except:
        break

    page_no+=1




    

