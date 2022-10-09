import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://paypay.yahoo.co.jp/balance')

wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
element = driver.find_element(By.NAME, "login")
element.send_keys(os.environ['NAME'])
time.sleep(0.1)

element = driver.find_element(By.NAME, "btnNext")
element.click()
time.sleep(0.1)

element = driver.find_element(By.NAME, "passwd")
element.send_keys(os.environ['PW'])
time.sleep(0.1)

element = driver.find_element(By.NAME, "btnSubmit")
element.click()

wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balTotal__number")))
element = driver.find_element(By.CLASS_NAME, "balTotal__number")

print(element.text)
