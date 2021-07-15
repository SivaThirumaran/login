from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import XLutils
import SS as S
import unittest
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager

from readProperties import Readconfig

class zipcodepage(unittest.TestCase):

    @staticmethod
    def test_zipcode():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/zipcode.xlsx"
        driver.zp = Registerpage(driver)

        driver.rows=XLutils.getRowCount(path ,'Sheet1')
        print("number of rows in excel:",driver.rows)

        for r in range(2, driver.rows + 1):
            driver.zipcode = XLutils.readData(path, 'Sheet1', r, 1)
            driver.exp = XLutils.readData(path, 'Sheet1', r, 2)

            driver.zp.setpincode(driver.zipcode)
            time.sleep(5)
            driver.zp.clicksubmit()
            '''navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            backendPerformance_calc = responseStart - navigationStart
            print(backendPerformance_calc / 1000)'''
            driver.quit()
            time.sleep(5)

            act_title = driver.title
            exp_title = "Standard Delivery - OrgFarm"
            log_file = "C:\\New folder\\seleniumdata\\Logs\\zipcode1.log"


            if act_title == exp_title:
                time.sleep(5)
                pass_message = "logs successful"
                U.log("INFO", pass_message, log_file)
                driver.zp.clickLocation()
                time.sleep(5)
                driver.zp.clickCHGlocation();

            else:
                S.screenshot(driver)
                time.sleep(5)
                message = driver.find_element_by_xpath('//*[@class="sweet-alert showSweetAlert visible"]//*[text()="Sorry We Do not Deliver to this Area Now"]')
                fail_message = message.text
                U.log("WARNING", fail_message + str(driver.zipcode), log_file)
                driver.zp.clickCLOSEbutton();


if __name__ == '__main__':
    unittest.main()
#if __name__=='__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))