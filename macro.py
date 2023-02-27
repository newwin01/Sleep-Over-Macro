import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# input = hisnet id & password
hisnet_id = input("Enter hisnet id: ")
hisnet_pw = input("Enter hisnet pw: ")

print(hisnet_id)
print(hisnet_pw)

# use chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

URL = 'https://hisnet.handong.edu/'

driver.get(URL)

# open URL
# URL = 'https://rc.handong.edu/rc/mypage/domExeat/index.do?menu_idx=70'
time.sleep(5)

# enter user data - login in to hisnet

# elem = driver.find_element(By.CSS_SELECTOR, "id")
# elem.click()

frame = driver.find_element(by=By.NAME, value="MainFrame")
driver.switch_to.frame(frame)

time.sleep(5)

# driver.switch_to

log_ID = driver.find_element(by = By.NAME, value = "id")
log_ID.send_keys(hisnet_id)

log_PW = driver.find_element(by= By.NAME, value= "password")
log_PW.send_keys(hisnet_pw)

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/2012_images/intro/btn_login.gif"]'))).click()

time.sleep(5)

# driver.find_element(By.NAME("password")).send_keys(str(hisnet_pw))

# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/2012_images/intro/btn_login.gif"]'))).click()


# driver.implicitly_wait(time_to_wait=20)


# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)

# browser.get()