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
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from custLogger import LogGen


class loginpage(unittest.TestCase):


    @staticmethod
    def test_login():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        driver.zp = Registerpage(driver)
        path = ".//testdata/logindata.xlsx"
        log_file = "C:\\New folder\\seleniumdata\\Logs\\coupon.log"
        driver.rows = XLutils.getRowCount(path, 'Sheet3')
        print("number of rows in excel:", driver.rows)

        for r in range(2, driver.rows + 1):
            driver.zp.clicksignin()
            time.sleep(2)
            driver.zp.clickloginwithpw()
            time.sleep(2)

            driver.zp.setemail('7010566308')
            driver.zp.setpassword('11223344')
            time.sleep(2)
            driver.zp.clicksign()
            time.sleep(5)

            try:
                driver.find_element_by_xpath("//a[contains(@class,'my-account-dropdown_class')]")
                #pass_message = "login successful"
                #U.log("INFO", pass_message, log_file)

                driver.zp.setpincode('600009')
                time.sleep(3)
                driver.zp.clicksubmit()
                time.sleep(5)

                act_title = driver.title
                exp_title = "Standard Delivery - OrgFarm"

                if act_title == exp_title:
                    #pass_message = "zipcode successful"
                    #U.log("INFO", pass_message, log_file)
                    time.sleep(5)
                    driver.find_element_by_xpath("//*[@id='sticky-wrapper']/div/div[2]/div[2]/ul/li[4]/a").click()
                    time.sleep(10)
                    driver.find_element_by_xpath('//*[@id="wrapper"]/div/div/div[2]/div[2]/div/div[5]/div[2]/a/div/img').click()
                    time.sleep(5)
                    driver.find_element(By.ID, "add-btn").click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="add-btn-container"]/a/span[4]').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="add-btn-container"]/a/span[4]').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="add-btn-container"]/a/span[4]').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="add-btn-container"]/a/span[4]').click()
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="mini-cart-button"]').click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="proceed_to_checkout_button"]').click()
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="address-panel"]/div[2]/div/h3').click()
                    time.sleep(3)
                    driver.couponcode = XLutils.readData(path, 'Sheet3', r, 1)
                    driver.zp.setCouponcode(driver.couponcode)
                    #driver.find_element_by_id('coupon').send_keys('jundt')
                    time.sleep(2)
                    driver.zp.clickApplyCoupon()
                    #driver.find_element_by_id('promo-form-button').click()
                    time.sleep(2)
                    try:
                        driver.find_element_by_xpath('//*[@id="checkout-total-wrapper"]/div[1]/div[3]')
                        message = driver.find_element_by_xpath('//*[@class="promo-code-success-message"]')
                        success_message = message.text
                        U.log("INFO", success_message, log_file)

                    except NoSuchElementException:
                        message = driver.find_element_by_xpath('//*[@class="promo-code-message"]')
                        invalid_message = message.text
                        U.log("WARNING", invalid_message, log_file)


                    find = driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]')
                    driver.execute_script("arguments[0].scrollIntoView();", find)
                    time.sleep(5)
                    driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]').click()
                    time.sleep(2)
                    driver.find_element(By.ID, 'button-confirm').click()
                    time.sleep(8)
                    driver.zp.clickHomeButton()
                    driver.zp.clickLocation()
                    time.sleep(2)
                    driver.zp.clickCHGlocation()
                    #driver.find_element_by_xpath('//*[@id="sticky-wrapper"]/div/div[1]/div[1]/div[1]/a/img').click()
                    driver.zp.clickAccount()
                    driver.zp.clickLogout();


                else:
                    time.sleep(2)
                    S.screenshot(driver)
                    #message = driver.find_element_by_xpath('/html/body/div[16]/h2')
                    #fail_message = message.text
                    #U.log("WARNING", fail_message , log_file)
                    time.sleep(5)
                    driver.zp.clickCLOSEbutton()


            except NoSuchElementException:
                act_title = driver.title
                exp_title = "Checkout - OrgFarm"

                if act_title == exp_title:
                    driver.find_element(By.XPATH, '//*[@id="address-panel"]/div[2]/div/h3').click()
                    time.sleep(3)
                    driver.find_element_by_id('coupon').send_keys('jundt')
                    time.sleep(2)
                    driver.find_element_by_id('promo-form-button').click()
                    time.sleep(2)
                    find = driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]')
                    driver.execute_script("arguments[0].scrollIntoView();", find)
                    time.sleep(5)
                    driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]').click()
                    time.sleep(2)
                    driver.find_element(By.ID, 'button-confirm').click()
                    time.sleep(8)
                    driver.find_element_by_xpath('//*[@id="sticky-wrapper"]/div/div[1]/div[1]/div[1]/a/img').click()
                    time.sleep(2)
                    driver.zp.clickAccount()
                    driver.zp.clickLogout();


                else:
                    S.screenshot(driver)
                    #message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
                    #fail_message = message.text
                    #U.log("WARNING", fail_message, log_file)
                    driver.zp.clickAccount()
                    driver.zp.clickLogout();

if __name__ == '__main__':
    unittest.main()
#if __name__=='__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))