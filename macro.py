import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# input = hisnet id & password
hisnet_id = input("Enter hisnet id: ")
hisnet_pw = input("Enter hisnet pw: ")

#check the info
print(hisnet_id)
print(hisnet_pw)

# use chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

URL = 'https://hisnet.handong.edu/'

#access to the homepage
driver.get(URL)
time.sleep(1)

# enter user data - login in to hisnet
frame = driver.find_element(by=By.NAME, value="MainFrame")
driver.switch_to.frame(frame)

log_ID = driver.find_element(by = By.NAME, value = "id")
log_ID.send_keys(hisnet_id)

log_PW = driver.find_element(by= By.NAME, value= "password")
log_PW.send_keys(hisnet_pw)

#login to hisnet by clicking
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/2012_images/intro/btn_login.gif"]'))).click()
time.sleep(3)

#Access to RC page
driver.execute_script('sendit12()')

time.sleep(3)