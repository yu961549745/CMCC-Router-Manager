from selenium import webdriver
import time
import datetime
import re
from password import username, password


def sleep():
    time.sleep(0.1)


def get_connect_time(no_ui=True):
    chrome_driver_path = './chromedriver'
    login_url = 'http://192.168.1.1/'

    options = webdriver.ChromeOptions()
    if no_ui:
        options.add_argument('headless')

    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(login_url)

    elem = driver.find_element_by_id("Frm_Username")
    elem.clear()
    elem.send_keys(username)

    elem = driver.find_element_by_id("Frm_Password")
    elem.clear()
    elem.send_keys(password)

    driver.find_element_by_id("LoginId").click()
    sleep()

    driver.switch_to.frame(driver.find_element_by_id("mainFrame"))
    sleep()

    if len(driver.find_elements_by_id("smWanStatu")) != 0:
        driver.find_element_by_id("smWanStatu").click()
        sleep()

    elem = driver.find_element_by_css_selector(
        "#TestContent tr:last-child td:last-child")
    time_str = elem.text

    if not no_ui:
        input()
    driver.close()

    p = re.search(r'(\d+)\s*秒', time_str)
    if p is not None:
        return str(datetime.timedelta(seconds=int(p.group(1))))
    else:
        return "[TIME NOT FOUND]->" + time_str
