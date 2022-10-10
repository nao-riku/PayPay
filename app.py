import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime
import time

n = datetime.datetime.now() + datetime.timedelta(hours=4)
end = datetime.datetime(n.year, n.month, n.day, n.hour, 10, 0)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',options=options)

def main(bal):
    while True:
      time.sleep(10)
      if datetime.datetime.now() > end:
        driver.quit()
        break
      loop(bal)

def loop(bal):
  global driver
  driver.refresh()
  try:
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balDetail__number")))
  except:
    html = driver.page_source
    time.sleep(2)
    print(html)
    time.sleep(60)
  else:
    element = driver.find_elements(By.CLASS_NAME, "balDetail__number")[1]
    bal2 = element.text
    if bal != bal2:
      bal = bal2
      r = requests.get(os.environ['URL'], params={"p": bal})
      print(bal)

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
  wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balDetail__number")))
  element = driver.find_elements(By.CLASS_NAME, "balDetail__number")[1]

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

  wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "balDetail__number")))
  element = driver.find_elements(By.CLASS_NAME, "balDetail__number")[1]
  
finally:
  bal = element.text
  r = requests.get(os.environ['URL'], params={"p": bal})
  print(bal)
  time.sleep(10)
  main(bal)
  
  


