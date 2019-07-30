from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


root_url = 'https://login.taobao.com/member/login.jhtml'
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('--start-maximized')

# 设置开发者模式启动，该模式下webdriver属性为正常值
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 禁止图片加载
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(options=options)

browser.implicitly_wait(10)
browser.get(root_url)

wait = WebDriverWait(browser, 10)


j_login_box = browser.find_element_by_id('J_Quick2Static')
ActionChains(browser).click(j_login_box).perform()

acount = browser.find_element_by_id('TPL_username_1')
print('acount')
acount.send_keys('798456988@qq.com')

password = browser.find_element_by_id('TPL_password_1')
print('password')
password.send_keys('123456789')

# browser.refresh()
