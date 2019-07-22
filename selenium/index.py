from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
inpurt = browser.find_element_by_id('kw')
inpurt.send_keys('Python')
inpurt.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)

print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
