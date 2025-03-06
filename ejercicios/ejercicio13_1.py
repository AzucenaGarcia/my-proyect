#input-example > button

"""https://the-internet.herokuapp.com/dynamic_controls"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")


time.sleep(5)
boton_enable = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
boton_enable.click()
time.sleep(5)


#input-example > input[type=text]
