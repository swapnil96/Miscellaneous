from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
browser = webdriver.Firefox()
browser.get("https://proxy22.iitd.ernet.in/squish/") 
time.sleep(10)
username = browser.find_element_by_name("uid")
password = browser.find_element_by_name("magic_word")
u = raw_input()
p = raw_input()
username.send_keys(u)
password.send_keys(p)
login_attempt = browser.find_element_by_name("1")
login_attempt.submit()
proxy = browser.find_element_by_xpath('//center/table[2]/tbody/tr[3]/td[3]')
print proxy.text
browser.close()
display.stop()