from selenium import webdriver
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path="D:\driver\geckodriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("TestComplated")

    def test_login(self,test_setup):
        driver.get('https://www.google.com/')
        driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
        print(driver.title)

    #def test_close():
    #   driver.close()
        #driver.quit()
     #  print("TestComplated")