from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import configuration
import XLutils
import SS as S
from selenium.common.exceptions import NoSuchElementException
from readProperties import Readconfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\python\Scripts\chromedriver.exe")

driver.get("https://staging.orgfarm.store/")
driver.maximize_window()
time.sleep(5)
driver.zp = Registerpage(driver)

driver.zp.clicksignin()
time.sleep(2)
driver.zp.clickloginwithpw()
time.sleep(2)
driver.zp.setemail('7010566308')
driver.zp.setpassword('11223344')
time.sleep(2)
driver.zp.clicksign()
time.sleep(2)
log_file = "C:\\New folder\\seleniumdata\\RegPage\\logins.log"
try:
    driver.find_element_by_xpath("//a[contains(@class,'my-account-dropdown_class')]")
    pass_message = "login successful"
    U.log("INFO", pass_message, log_file)
    time.sleep(2)
    driver.zp.setpincode('600000')
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
        driver.find_element(By.XPATH, "//*[@id='wrapper']/div/div/div[2]/div[2]/div/div[3]/div[2]/div/h3/a[2]").click()
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
        driver.find_element(By.ID, 'button-confirm').click()


    else:
        time.sleep(2)
        S.screenshot(driver)
        message = driver.find_element_by_xpath('/html/body/div[14]/h2')
        fail_message = message.text
        U.log("WARNING", fail_message, log_file)
        time.sleep(5)


except NoSuchElementException:
    S.screenshot(driver)
    message = driver.find_element_by_xpath('//*[@id="login-message"]/p')
    fail_message = message.text
    U.log("WARNING", fail_message , log_file);
