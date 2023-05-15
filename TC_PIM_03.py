from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(15)

#TC_login_01
#username Admin
username=driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("Admin")

#password Admin123
password=driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("admin123")

#login_btn
login_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
login_btn.click()

act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("test case is passed")
else:
    print("test case is failed")

time.sleep(10)
#switching dashboard to pim module
switch_frame=driver.switch_to.parent_frame()


#pim mopdule details
pim=driver.find_element(By.XPATH,"//span[normalize-space()='PIM']")
pim.click()
time.sleep(5)


#search employee from employee list
ser_emp_NaMe=driver.find_element(By.XPATH,'//input[@placeholder="Type for hints..."]')
ser_emp_NaMe.send_keys("Yogesh")

driver.find_element(By.XPATH,'//button[@type="submit"]')
driver.click()

del_button=driver.find_element(By.XPATH,'//button[@type="button"]')
del_button.click()

delete=driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div/div/div[3]/button[2]')
delete.click()


