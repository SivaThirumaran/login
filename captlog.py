import pytest
from selenium import webdriver
from element import Registerpage
import time
import SS as S
from selenium.common.exceptions import NoSuchElementException
import Utilities as U
import XLutils
import unittest
import HtmlTestRunner
import unittest_parallel

class loginpagee(unittest.TestCase):

    @staticmethod
    def test_login():
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\python\Scripts\chromedriver.exe")
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/logindata.xlsx"
        driver.zp = Registerpage(driver)
        log_file = "C:\\New folder\\seleniumdata\\RegPage\\loginpage11.log"
        driver.rows = XLutils.getRowCount(path ,'Sheet1')
        print("number of rows in excel:",driver.rows)

        for r in range(2, driver.rows + 1):
            driver.zp.clicksignin()
            time.sleep(2)
            driver.zp.clickloginwithpw()
            time.sleep(2)
            driver.Email = XLutils.readData(path, 'Sheet1', r, 1)
            driver.Password = XLutils.readData(path, 'Sheet1', r, 2)
            driver.exp = XLutils.readData(path, 'Sheet1', r, 3)

            driver.zp.setemail(driver.Email)
            time.sleep(2)
            driver.zp.setpassword(driver.Password)
            time.sleep(2)
            driver.zp.clicksign()
            time.sleep(5)

            try:
                driver.find_element_by_xpath("//a[contains(@class,'my-account-dropdown_class')]")
                pass_message = "login successful"
                U.log("INFO", pass_message, log_file)
                print(pass_message)
                driver.zp.clickAccount()
                time.sleep(2)
                driver.zp.clickLogout();

            except NoSuchElementException:
                S.screenshot(driver)
                message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
                fail_message = message.text
                U.log("WARNING", fail_message, log_file)
                print(fail_message)
                driver.zp.clickBackButton();
'''
    @staticmethod
    def test_zipcode():
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\python\Scripts\chromedriver.exe")
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/logindata.xlsx"
        driver.zp = Registerpage(driver)
        log_file = "C:\\New folder\\seleniumdata\\RegPage\\loginpage.log"
        driver.rows = XLutils.getRowCount(path, 'Sheet2')
        print("number of rows in excel:", driver.rows)

        for r in range(2, driver.rows + 1):
            driver.zipcode = XLutils.readData(path, 'Sheet2', r, 1)
            driver.exp = XLutils.readData(path, 'Sheet2', r, 2)

            driver.zp.setpincode(driver.zipcode)
            time.sleep(3)
            driver.zp.clicksubmit()
            time.sleep(5)

            act_title = driver.title
            exp_title = "Standard Delivery - OrgFarm"

            if act_title == exp_title:
                time.sleep(2)
                pass_message = "zipcode successful"
                U.log("INFO", pass_message, log_file)
                driver.zp.clickLocation()
                time.sleep(5)
                driver.zp.clickCHGlocation();

            else:
                time.sleep(2)
                S.screenshot(driver)
                message = driver.find_element_by_xpath('/html/body/div[14]/h2')
                fail_message = message.text
                U.log("WARNING", fail_message, log_file)
                time.sleep(5)
                driver.zp.clickCLOSEbutton();'''

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))