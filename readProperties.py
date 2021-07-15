import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\confg.ini")

class Readconfig:
    @staticmethod
    def getapplicationURL():
        url = config.get('login info', 'baseurl')
        return url

    @staticmethod
    def getfirstname():
        userfirstname = config.get('login info', 'firstname')
        return userfirstname

    @staticmethod
    def getlastname():
        userlastname = config.get('login info', 'lastname')
        return userlastname

    @staticmethod
    def getemailaddress():
        useremailaddress = config.get('login info', 'emailaddress')
        return useremailaddress

    @staticmethod
    def getpassword():
        userpassword = config.get('login info', 'password')
        return userpassword

    @staticmethod
    def getphonenumber():
        userphonenumber = config.get('login info', 'phonenumber')
        return userphonenumber

    @staticmethod
    def getemail():
        useremail = config.get('login info', 'email')
        return useremail

    @staticmethod
    def getpincode():
        userpincode = config.get('login info', 'pincode')
        return userpincode