"""https://the-internet.herokuapp.com/dynamic_controls"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

boton_checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox").click()
time.sleep(5)
boton_remove = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
boton_remove.click()
time.sleep(5)



boton_add = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
boton_add.click()
time.sleep(5)