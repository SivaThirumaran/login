from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import XLutils
import SS as S

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\python\Scripts\chromedriver.exe")

driver.get("https://staging.orgfarm.store/")
driver.maximize_window()
path = ".//testdata/RegisterData.xlsx"
driver.zp = Registerpage(driver)

driver.rows=XLutils.getRowCount(path ,'Sheet1')
print("number of rows in excel:",driver.rows)

for r in range(6, driver.rows + 1):

    driver.zp.clickRegisterButton()

    driver.FirstName = XLutils.readData(path, 'Sheet1', r, 1)
    driver.LastName = XLutils.readData(path, 'Sheet1', r, 2)
    driver.EmailAddress = XLutils.readData(path, 'Sheet1', r, 3)
    driver.PassWorD = XLutils.readData(path, 'Sheet1', r, 4)
    driver.PhoneNumber = XLutils.readData(path, 'Sheet1', r, 5)
    driver.exp = XLutils.readData(path, 'Sheet1', r, 6)

    driver.zp.setFistName(driver.FirstName)
    driver.zp.setLastName(driver.LastName)
    driver.zp.setEmailAddress(driver.EmailAddress)
    driver.zp.setPassWord(driver.PassWorD)
    driver.zp.setPhoneNum(driver.PhoneNumber)
    time.sleep(5)
    find = driver.find_element_by_xpath('//*[@id="signup"]')
    driver.execute_script("arguments[0].scrollIntoView();", find)
    driver.find_element_by_xpath('//*[@id="signup"]').click()

    result = driver.find_element_by_xpath('//*[@id="signupModal-popup"]/div/div/div/div[2]/div/div[1]/h4')

    exp_result = "Signup"
    log_file = "C:\\New folder\\seleniumdata\\RegPage\\all.log"


    if result.text == exp_result:
        if driver.exp == "Pass":
            time.sleep(2)
            pass_message = "logs successful"
            U.log("INFO", pass_message, log_file)
            driver.zp.clickOTPpageBack();

        elif driver.exp == "Fail":
            S.screenshot(driver)
            time.sleep(2)
            email = driver.find_element_by_xpath('//*[@id="other_signup_div"]/div[3]/div/p')
            email_message = email.text
            time.sleep(2)
            U.log("WARNING",email_message + driver.EmailAddress ,log_file)
            driver.zp.clickBackButton();

    '''elif result.text != exp_result:
        if driver.exp == "Pass":
            time.sleep(2)
            S.screenshot(driver)
            U.log("INFO", fail_message, log_file)
            driver.zp.clickOTPpageBack();

        elif driver.exp == "Fail":
            time.sleep(2)
            S.screenshot(driver)
            U.log("INFO", pass_message, log_file)
            driver.zp.clickBackButton();'''
