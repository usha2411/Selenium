import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
time.sleep(2)
a=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(a))
for i in a:
    if i.text=="Russia":
        i.click()
        break
time.sleep(2)