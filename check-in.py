from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys
from decouple import config

#####
user = config('USERNAME')
passwd = config('PASSWORD')
#####
# driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
url = 'https://leetcode.com/accounts/login/'
driver.get(url)
username = driver.find_element_by_id('id_login')
username.send_keys(user)
password = driver.find_element_by_id('id_password')
password.send_keys(passwd)
btn = driver.find_element_by_xpath('//button[@class="btn btn-primary sign-in-btn"]')
btn.click()

try:
	WebDriverWait(driver, 40).until(EC.title_contains('LeetCode'))
except TimeoutException:
	print('Login failed')
	driver.quit()
	sys.exit()

time.sleep(5)
print('Done!')
driver.quit()


### EOF