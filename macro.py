import time
from datetime import datetime
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def macro():
    # input = hisnet id & password
    hisnet_id = input("Enter hisnet id: ")
    hisnet_pw = input("Enter hisnet pw: ")

    # input = sleepover location & reason
    location = input("Enter the location of sleepover: ")
    reason = input("Enter the reason of sleepover: ")

    # check the info
    log_writer(0, hisnet_id)
    log_writer(0, hisnet_pw)

    # use chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("headless") #make chrome to execute on background
    driver = webdriver.Chrome(options=options)

    URL = 'https://hisnet.handong.edu/'

    # access to the homepage
    driver.get(URL)
    time.sleep(1)

    # enter user data - login in to hisnet
    frame = driver.find_element(by=By.NAME, value="MainFrame")
    driver.switch_to.frame(frame)

    log_ID = driver.find_element(by = By.NAME, value = "id")
    log_ID.send_keys(hisnet_id)

    log_PW = driver.find_element(by= By.NAME, value= "password")
    log_PW.send_keys(hisnet_pw)

    # login to hisnet by clicking
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="/2012_images/intro/btn_login.gif"]'))).click()
    time.sleep(0.5)

    # access to RC page
    driver.execute_script('sendit12()')

    # close hisnet tab and swith to open tab
    driver.close() 
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab )

    # access to my page
    time.sleep(1)
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="header"]/div/div/div[2]/ul/li[2]/a'))).click()

    # access to sleepover registration page
    time.sleep(1)
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mypage"]/div[2]/div[3]/dl[3]/dd/a'))).click()

    # click date
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ovng_begin_dttm"]'))).click()

    CurrentDay = date.today().day
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ovng_begin_dttm"]'))).click()

    time.sleep(1)

    # enter text - data(location; reason)
    log_writer(0, location)
    log_writer(0, reason)
    conjunction = "에서 "
    data = location + conjunction + reason

    Reason_text = driver.find_element(by = By.NAME, value = "ovng_resn")
    Reason_text.send_keys(data)

    time.sleep(1)

    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.LINK_TEXT, str(CurrentDay)))).click()

    # click apply
    WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="domExeat"]/div[2]/button'))).click()
    # time.sleep(1)

    # wait for reloading to repeat
    # Congratulations~~
    time.sleep(3)



# 0 for INFO, 1 for WARN, 2 for ERROR
def log_writer(log_code:int, msg:str):
    message = ''
    if log_code == 0:
        message += ':::INFO:::|'
    elif log_code == 1:
        message += ':::WARN:::|'
    elif log_code == 2:
        message += ':::ERROR:::|'
    message += datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '|' + msg
    print(message)



if __name__ == '__main__':
    macro()