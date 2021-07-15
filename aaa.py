from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import XLutils
import SS as S
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from readProperties import Readconfig

from webdriver_manager.chrome import ChromeDriverManager




def test_log():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://staging.orgfarm.store/")
    driver.maximize_window()
    path = ".//testdata/logindata.xlsx"
    driver.zp = Registerpage(driver)
    log_file = "C:\\New folder\\seleniumdata\\RegPage\\logins.log"
    driver.rows=XLutils.getRowCount(path ,'Sheet1')
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
            path = ".//testdata/zipcode.xlsx"
            driver.zp = Registerpage(driver)

            driver.rows = XLutils.getRowCount(path, 'Sheet1')
            print("number of rows in excel:", driver.rows)

            for r in range(2, driver.rows + 1):
                driver.zipcode = XLutils.readData(path, 'Sheet1', r, 1)
                driver.exp = XLutils.readData(path, 'Sheet1', r, 2)

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
                    time.sleep(5)
                    driver.find_element_by_xpath("//*[@id='sticky-wrapper']/div/div[2]/div[2]/ul/li[4]/a").click()
                    time.sleep(5)
                    driver.find_element(By.XPATH,
                                        "//*[@id='wrapper']/div/div/div[2]/div[2]/div/div[3]/div[2]/div/h3/a[2]").click()
                    time.sleep(2)
                    driver.find_element(By.ID, "add-btn").click()
                    driver.find_element(By.CLASS_NAME, 'unique_plus_button2084-0').click()
                    driver.find_element(By.CLASS_NAME, 'unique_plus_button2084-0').click()
                    time.sleep(3)
                    driver.find_element(By.ID, 'mini-cart-button').click()
                    driver.find_element(By.ID, 'proceed_to_checkout_button').click()
                    time.sleep(3)
                    driver.find_element(By.XPATH, '//*[@id="address-panel"]/div[2]/div/h3').click()
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
                    U.log("WARNING", fail_message + str(driver.zipcode), log_file)
                    time.sleep(5)
                    driver.zp.clickCLOSEbutton();

        except NoSuchElementException:
            S.screenshot(driver)
            message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
            fail_message = message.text
            U.log("WARNING", fail_message , log_file);
