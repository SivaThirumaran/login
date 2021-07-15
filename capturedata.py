from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.co.in/")
time.sleep(5)
driver.find_element_by_name("q").send_keys("selen")
p1 = driver.find_elements_by_xpath("//*[@class='sbct']")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(5)
driver.quit()