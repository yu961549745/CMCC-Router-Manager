from selenium import webdriver
from password import username, password

chrome_driver_path = './chromedriver'
login_url = 'http://192.168.1.1/'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(login_url)

elem = driver.find_element_by_id("Username")
elem.clear()
elem.send_keys(username)

elem = driver.find_element_by_id("Password")
elem.clear()
elem.send_keys(password)

driver.find_element_by_id("btnSubmit").click()
