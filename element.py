class Registerpage:
    button_RegisterButton_xpath = "/html/body/div[1]/div[1]/div/div/div[2]/div/div/a[3]"
    textbox_first_name_ID = "FirstName"
    textbox_last_name_ID = "LastName"
    textbox_Email_add_xpath = '//*[@class="col-md-12 no-pad register-user"]//*[@id="email"]'
    textbox_password_ID = "password"
    textbox_phoneNum_ID = "register_phone_number"
    button_CreateAcc_ID = "//*[@id='signup']"
    textbox_SignOTP_ID = "signup_otp"
    textVisible_SignUp_xpath = '//*[@id="signupModal-popup"]/div/div/div/div[2]/div/div[1]/h4'
    button_OTPpageBackButton_xpath = '//*[@id="signupModal-popup"]/div/div/div/div[1]/img'
    button_SignUpBackButton_xpath = '//*[@id="signupModal-popup"]/div/div/div/div[1]/img'
    button_Visible_xpath = '//*[@id="signup_otp"]'
    button_SiginPageBack_xpath = '//*[@id="loginpasswordModal"]/div/div/div/div[1]/img'
    button_signin_xpath="/html/body/div[1]/div[1]/div/div/div[2]/div/div/a[2]"
    button_login_with_pw_xpath='//*[@id="login-form"]/div/div[2]/div/a'
    textbox_email_name="email"
    textbox_password_name="password"
    button_sign_name="login"
    textbox_pincode_id="searchTextField"
    button_start_xpath="//*[@id='submit']"
    button_Account_xpath="//a[contains(@class,'my-account-dropdown_class')]"
    button_Logout_xpath='//a[@href="https://staging.orgfarm.store/logout"]'
    button_Location_xpath="//*[@id='sticky-wrapper']/div/div[1]/div[2]/div[3]/a[1]"
    button_CHGLocation_xpath="//*[@id='useraddress-popup']/div/div/div/div/div/div/a"
    button_CLRpincode_name="zipcode"
    button_CLOSEbutton_xpath="//*[@class='confirm']"
    textbox_Coupon_id='coupon'
    button_CouponApply_id='promo-form-button'
    button_logoHomebutton_xpath='//*[@id="sticky-wrapper"]/div/div[1]/div[1]/div[1]/a/img'
    Get_tagname = "a"


    def __init__(self,driver):
        self.driver=driver

    def clickRegisterButton(self):
        self.driver.find_element_by_xpath(self.button_RegisterButton_xpath).click()

    def setFistName(self,firstname):
        self.driver.find_element_by_id(self.textbox_first_name_ID).clear()
        self.driver.find_element_by_id(self.textbox_first_name_ID).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_id(self.textbox_last_name_ID).clear()
        self.driver.find_element_by_id(self.textbox_last_name_ID).send_keys(lastname)

    def setEmailAddress(self,emailaddress):
        #self.driver.find_element_by_id(self.textbox_Email_add_ID).clear()
        self.driver.find_element_by_xpath(self.textbox_Email_add_xpath).send_keys(emailaddress)

    def setPassWord(self,password):
        self.driver.find_element_by_id(self.textbox_password_ID).clear()
        self.driver.find_element_by_id(self.textbox_password_ID).send_keys(password)

    def setPhoneNum(self,phonenumber):
        self.driver.find_element_by_id(self.textbox_phoneNum_ID).clear()
        self.driver.find_element_by_id(self.textbox_phoneNum_ID).send_keys(phonenumber)

    def CreateAcc(self):
        self.driver.find_element_by_id(self.button_CreateAcc_ID)

    def clickCreateAcc(self):
        self.driver.find_element_by_id(self.button_CreateAcc_ID).click()

    def setSignOTP(self):
        self.driver.find_element_by_id(self.textbox_SignOTP_ID)

    def textSignIn(self):
        self.driver.find_element_by_id(self.textVisible_SignUp_xpath)

    def clickOTPpageBack(self):
        self.driver.find_element_by_xpath(self.button_OTPpageBackButton_xpath).click()

    def clickSignUpBack(self):
        self.driver.find_element_by_xpath(self.button_SignUpBackButton_xpath).click()

    def visibleText(self):
        self.driver.find_element_by_xpath(self.button_Visible_xpath).click()

    def clickBackButton(self):
        self.driver.find_element_by_xpath(self.button_SiginPageBack_xpath).click()

    def clicksignin(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def clickloginwithpw(self):
        self.driver.find_element_by_xpath(self.button_login_with_pw_xpath).click()

    def setemail(self,email):
        self.driver.find_element_by_name(self.textbox_email_name).clear()
        self.driver.find_element_by_name(self.textbox_email_name).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    def clicksign(self):
        self.driver.find_element_by_name(self.button_sign_name).click()

    def setpincode(self,pincode):
        self.driver.find_element_by_id(self.textbox_pincode_id).clear()
        self.driver.find_element_by_id(self.textbox_pincode_id).send_keys(pincode)

    def clicksubmit(self):
        self.driver.find_element_by_xpath(self.button_start_xpath).click()

    def clickAccount(self):
        self.driver.find_element_by_xpath(self.button_Account_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_Logout_xpath).click()

    def clickLocation(self):
        self.driver.find_element_by_xpath(self.button_Location_xpath).click()

    def clickCHGlocation(self):
        self.driver.find_element_by_xpath(self.button_CHGLocation_xpath).click()

    def clickCLRpincode(self):
        self.driver.find_element_by_name(self.button_CLRpincode_name).clear()

    def clickCLOSEbutton(self):
        self.driver.find_element_by_xpath(self.button_CLOSEbutton_xpath).click()

    def clearEmail(self):
        self.driver.find_element_by_name(self.textbox_email_name).clear()

    def clearPassword(self):
        self.driver.find_element_by_name(self.textbox_password_name).clear()

    def getlink(self):
        self.driver.find_elements_by_tag_name(self.Get_tagname)

    def setCouponcode(self,couponcode):
        self.driver.find_element_by_id(self.textbox_Coupon_id).clear()
        self.driver.find_element_by_id(self.textbox_Coupon_id).send_keys(couponcode)

    def clickApplyCoupon(self):
        self.driver.find_element_by_id(self.button_CouponApply_id).click()

    def clickHomeButton(self):
        self.driver.find_element_by_xpath(self.button_logoHomebutton_xpath).click()

