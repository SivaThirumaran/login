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


class loginpage(unittest.TestCase):


    @staticmethod
    def test_login():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://staging.orgfarm.store/")
        driver.maximize_window()
        driver.zp = Registerpage(driver)
        log_file = "C:\\New folder\\seleniumdata\\RegPage\\loginpage111.log"

        driver.zp.clicksignin()
        time.sleep(2)
        driver.zp.clickloginwithpw()
        time.sleep(2)

        driver.zp.setemail('7010566308')
        time.sleep(2)
        driver.zp.setpassword('11223344')
        time.sleep(2)
        driver.zp.clicksign()
        time.sleep(5)

        try:
            driver.find_element_by_xpath("//a[contains(@class,'my-account-dropdown_class')]")
            pass_message = "login successful"
            U.log("INFO", pass_message, log_file)

            driver.zp.setpincode('600009')
            time.sleep(3)
            driver.zp.clicksubmit()
            time.sleep(5)

            act_title = driver.title
            exp_title = "Standard Delivery - OrgFarm"

            if act_title == exp_title:
                time.sleep(2)
                pass_message = "zipcode successful"
                U.log("INFO", pass_message, log_file)
                time.sleep(5)
                driver.find_element_by_xpath("//*[@id='sticky-wrapper']/div/div[2]/div[2]/ul/li[4]/a").click()
                time.sleep(10)
                driver.find_element_by_xpath('//div[@data-item_model="Yelakki   "]').click()
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
                driver.find_element_by_id('coupon').send_keys('jundt')
                time.sleep(2)
                driver.find_element_by_id('promo-form-button').click()
                time.sleep(2)
                find = driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]')
                driver.execute_script("arguments[0].scrollIntoView();", find)
                time.sleep(5)
                driver.find_element(By.XPATH, '//*[@id="payment-method-wrapper"]/div/label[2]').click()
                time.sleep(2)
                driver.find_element(By.ID, 'button-confirm').click();
            else:
                time.sleep(2)
                S.screenshot(driver)
                message = driver.find_element_by_xpath('/html/body/div[16]/h2')
                fail_message = message.text
                U.log("WARNING", fail_message, log_file)
                time.sleep(5)
                driver.zp.clickCLOSEbutton()

        except NoSuchElementException:
            S.screenshot(driver)
            message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
            fail_message = message.text
            U.log("WARNING", fail_message, log_file);


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ELCOT\\PycharmProjects\\login\\reporttt'))