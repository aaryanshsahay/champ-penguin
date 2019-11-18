from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
 
usr=input('Enter email id:')
pwd=input('Enter Password:')


driver = webdriver.Chrome()
driver.get('https://www.facebook.com')
sleep(3)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
sleep(3)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_box = driver.find_element_by_id('u_0_b')
login_box.click()
