from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)

browser.get('https://www.baidu.com')
inpurt = browser.find_element_by_id('kw')
inpurt.send_keys('Python')
inpurt.send_keys(Keys.ENTER)

print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
