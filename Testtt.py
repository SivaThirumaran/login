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

class zipcodepage(unittest.TestCase):

    @staticmethod
    def test_zipcode():
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\python\Scripts\chromedriver.exe")
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/logindata.xlsx"
        driver.zp = Registerpage(driver)
        log_file = "C:\\New folder\\seleniumdata\\RegPage\\zipcode11.log"
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
                U.log('ZIPCODE' +"INFO", pass_message , log_file)
                driver.zp.clickLocation()
                time.sleep(5)
                driver.zp.clickCHGlocation();

            else:
                time.sleep(2)
                S.screenshot(driver)
                message = driver.find_element_by_xpath('/html/body/div[14]/h2')
                fail_message = message.text
                U.log('ZIPCODE' +"WARNING", fail_message + str(driver.zipcode), log_file)
                time.sleep(5)
                driver.zp.clickCLOSEbutton();

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))