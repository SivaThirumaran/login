from selenium import webdriver
import time
import Utilities as U
from element import Registerpage
import XLutils
import SS as S
import unittest
import HtmlTestRunner
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://staging.orgfarm.store/")
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
backendPerformance_calc = responseStart - navigationStart
print(backendPerformance_calc / 1000)