import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=options)
driver.get('https://paypay.yahoo.co.jp/balance')

wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
element = driver.find_element(By.NAME, "login")
element.send_keys(os.environ['NAME'])
time.sleep(1)

element = driver.find_element(By.NAME, "btnNext")
element.click()
time.sleep(1)

element = driver.find_element(By.NAME, "passwd")
element.send_keys(os.environ['PW'])
time.sleep(1)

element = driver.find_element(By.NAME, "btnSubmit")
element.click()
time.sleep(1)

try:
  wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balTotal__number")))
  element = driver.find_element(By.CLASS_NAME, "balTotal__number")

except:
  element = driver.find_elements(By.NAME, "selectedQtype")[2]
  print(element)
  element.send_keys(Keys.SPACE)
  time.sleep(1)

  element = driver.find_element(By.NAME, "aqanswer")
  element.send_keys(os.environ['ADDRESS'])
  time.sleep(1)

  element = driver.find_element(By.NAME, "btnSubmit")
  element.click()
  time.sleep(1)

  wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balTotal__number")))
  element = driver.find_element(By.CLASS_NAME, "balTotal__number")

print(element.text)
