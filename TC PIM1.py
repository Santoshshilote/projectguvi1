import driver as driver
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
#add employee
add_emp=driver.find_element(By.LINK_TEXT,"Add Employee")
add_emp.click()
time.sleep(5)
#filling employee personal details
#first name
F_name=driver.find_element(By.XPATH,'//input[@placeholder="First Name"]')
F_name.send_keys("Santosh")
#middle name
M_name=driver.find_element(By.XPATH,'//input[@placeholder="Middle Name"]')
M_name.send_keys("A")
#last name
L_name=driver.find_element(By.XPATH,'//input[@placeholder="Last Name"]')
L_name.send_keys("Shilote")
time.sleep(5)



#filling personal details
#nickname
time.sleep(15)
nickname=driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")
nickname.send_keys("santu")

#otherid
other_id=driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")
other_id.send_keys("00012")

#license number
lic_no=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
lic_no.send_keys("1234565789")

#expiary date
exp=driver.find_element(By.XPATH,'//input[@placeholder="yyyy-mm-dd"]')
exp.send_keys("2024-09-16")


##ssnnumber
ssn_no=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input')
ssn_no.send_keys("1234")

#sin number
sin_no=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input')
sin_no.send_keys("2345")
#nationality

drp_nationality=Select(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div'))
drp_nationality.Select_by_visible_text("Indian")

#marital_status
marital_status=Select(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'))
marital_status.Select_by_visible_text("single")

#date of birth

exp=driver.find_element(By.XPATH,'//input[@placeholder="yyyy-mm-dd"]')
exp.send_keys("1995-09-16")

#gender
gen=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label')
gen.click()


militry_service=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div')
militry_service.send_keys("no")

s_btn=driver.find_element(By.XPATH,'//button[@type="submit"]')
s_btn.click()



