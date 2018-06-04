#!usr/bin/python

from selenium import webdriver

import time

driver=webdriver.Firefox()
driver.get("https://www.facebook.com/")

username = driver.find_element_by_id("email")
username.send_keys("*********@gmail.com")

password = driver.find_element_by_id("pass")
password.send_keys("***********")

login = driver.find_element_by_id("u_0_2")
login.click()
time.sleep(10)
driver.close()
