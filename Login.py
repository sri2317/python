from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path="D:\driver\geckodriver.exe")

#driver = webdriver.ie(executable_path="D:\driver\IEDriverServer_Win32_3.14.0\IEDriverServer.exe")

driver.get("https://xd.adobe.com/view/afbaca7f-1fef-4003-4112-29a7e3de6043-d98b/?fullscreen&hints=off")
print("Tile of the page : " + driver.title) # Tile of the page
print("URL of the page : " + driver.current_url) # returns the url of the page
driver.get("https://mastekgroup.sharepoint.com/pages/default.aspx")
print("Tile of the page : " + driver.title) # Tile of the page
print("URL of the page : " + driver.current_url) # returns the url of the page
time.sleep(10)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
