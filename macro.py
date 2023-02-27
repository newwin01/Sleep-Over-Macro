from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# input = hisnet id & password
hisnet_id = input("Enter hisnet id: ")
hisnet_pw = input("Enter hisnet pw: ")

# use chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

URL = 'https://hisnet.handong.edu/'

driver.get(URL)

# open URL
# URL = 'https://rc.handong.edu/rc/mypage/domExeat/index.do?menu_idx=70'


driver.implicitly_wait(time_to_wait=5)

# enter user data - login in to hisnet

id = driver.find_element(By.NAME, "id")
id.send_keys(hisnet_id)


driver.find_element(By.NAME("password")).send_keys(str(hisnet_pw))

# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/2012_images/intro/btn_login.gif"]'))).click()


driver.implicitly_wait(time_to_wait=20)


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)

# browser.get()