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

class registerpage(unittest.TestCase):

    @staticmethod
    def test_register():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        path = ".//testdata/RegisterData.xlsx"
        driver.zp = Registerpage(driver)

        driver.rows=XLutils.getRowCount(path ,'PhoneNum')
        print("number of rows in excel:",driver.rows)

        for r in range(2, driver.rows + 1):

            driver.zp.clickRegisterButton()

            driver.FirstName = XLutils.readData(path, 'PhoneNum', r, 1)
            driver.LastName = XLutils.readData(path, 'PhoneNum', r, 2)
            driver.EmailAddress = XLutils.readData(path, 'PhoneNum', r, 3)
            driver.PassWorD = XLutils.readData(path, 'PhoneNum', r, 4)
            driver.PhoneNumber = XLutils.readData(path, 'PhoneNum', r, 5)
            driver.exp = XLutils.readData(path, 'PhoneNum', r, 6)

            driver.zp.setFistName(driver.FirstName)
            driver.zp.setLastName(driver.LastName)
            driver.zp.setEmailAddress(driver.EmailAddress)
            driver.zp.setPassWord(driver.PassWorD)
            driver.zp.setPhoneNum(driver.PhoneNumber)
            time.sleep(5)
            find = driver.find_element_by_xpath('//*[@id="signup"]')
            driver.execute_script("arguments[0].scrollIntoView();", find)
            driver.find_element_by_xpath('//*[@id="signup"]').click()

            log_file = "C:\\New folder\\seleniumdata\\RegPage\\RegEmail.log"


            try:
                time.sleep(5)
                driver.find_element_by_xpath("//*[@class='fild_error']")
                S.screenshot(driver)
                time.sleep(2)
                phoneNum = driver.find_element_by_xpath("//*[@class='fild_error']")
                phoneNum_message = phoneNum.text
                time.sleep(2)
                U.log("WARNING", phoneNum_message + str(driver.PhoneNumber), log_file)
                time.sleep(2)
                driver.zp.clickSignUpBack();


            except NoSuchElementException:
                time.sleep(2)
                pass_message = "logs successful"
                U.log("INFO", pass_message, log_file)
                time.sleep(2)
                driver.zp.clickOTPpageBack();


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))