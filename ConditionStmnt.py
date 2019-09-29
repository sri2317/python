from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path="D:\driver\geckodriver.exe")
driver.get("http://newtours.demoaut.com/")
time.sleep(10)
user_ele = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input")
print(user_ele.is_displayed()) #returns true/false based
print("username field is enabled:",user_ele.is_enabled()) #returns true/false if filed enabled
pass_ele = driver.find_element_by_name("password")
print(pass_ele.is_displayed()) #returns true/false based
print(pass_ele.is_enabled()) #returns true/false if filed enabled
user_ele.send_keys("mercury")
pass_ele.send_keys("mercury")
#driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
driver.find_element_by_name("login").click()
radio1 = driver.find_element_by_css_selector("input[value='roundtrip']")
#radio1=driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]")
print("Round trip button is selected:",radio1.is_selected())
