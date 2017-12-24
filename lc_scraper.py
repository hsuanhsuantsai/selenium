from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import sys
from decouple import config

#####
user = config('USERNAME')
passwd = config('PASSWORD')
#####
driver = webdriver.Firefox()
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

url2 = 'https://leetcode.com/problemset/all/'
driver.get(url2)
try:
	WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="btn btn-xs btn-default round-btn tags-btn sm-company"]')))
except TimeoutException:
	print('No company shown')
	driver.quit()
	sys.exit()

company = driver.find_elements_by_xpath('//a[@class="btn btn-xs btn-default round-btn tags-btn sm-company"]')
url = []
for i in company:
	link = i.get_attribute('href')
	url.append(link)

# print(url)
for i in url:
	name = i.split('/')[-2]
	print(name)
	driver.get(i)
	elem = driver.find_elements_by_xpath('//td')
	data = []
	for j in range(0, int(len(elem)/6)):
		data.append(elem[j*6+1].text + '\t' + elem[j*6+2].text)
	with open(name+'.txt', 'w') as f:
		lines = map(lambda x: x+'\n', data)
		f.writelines(lines)

	time.sleep(10)

print('Done!')

driver.quit()


### EOF