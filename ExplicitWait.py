from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path="D:\driver\geckodriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")
#driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element_by_id("tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element_by_id("flight-origin-hp-flight").clear()
driver.find_element_by_id("flight-origin-hp-flight").send_keys("BOM")
driver.find_element_by_id("flight-destination-hp-flight").clear()
driver.find_element_by_id("flight-destination-hp-flight").send_keys("DEL")
driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("10/10/2019")
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").clear()
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").send_keys("10/11/2019")
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

#Explicit wait

wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops']/div/div[3]/div/label")))

element.click()

time.sleep(5)

driver.quit()

