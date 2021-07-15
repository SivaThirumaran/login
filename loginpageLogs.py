from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import XLutils
import SS as S
import unittest
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


from readProperties import Readconfig

class loginpage(unittest.TestCase):

    @staticmethod
    def test_login():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/logindata.xlsx"
        driver.zp = Registerpage(driver)

        driver.rows=XLutils.getRowCount(path ,'Sheet1')
        print("number of rows in excel:",driver.rows)

        for r in range(2, driver.rows+1):

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
            navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
            responseStart = driver.execute_script("return window.performance.timing.responseStart")
            backendPerformance_calc = responseStart - navigationStart
            print(backendPerformance_calc / 1000)
            #time.sleep(5)
            log_file = "C:\\New folder\\seleniumdata\\Logs\\login.log"


            try:
                driver.find_element_by_xpath("//a[contains(@class,'my-account-dropdown_class')]")
                pass_message = "login successful"
                U.log("INFO", pass_message, log_file)
                time.sleep(2)
                driver.zp.clickAccount()
                time.sleep(2)
                driver.zp.clickLogout();

            except NoSuchElementException:
                S.screenshot(driver)
                message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
                fail_message = message.text
                U.log("WARNING", fail_message, log_file);
                time.sleep(2)
                driver.zp.clickBackButton();

if __name__ == '__main__':
    unittest.main()
#if __name__=='__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))