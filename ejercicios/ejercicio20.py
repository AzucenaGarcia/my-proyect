import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu")


button  = driver.find_element(By.CSS_SELECTOR, "#ui-id-3 > a")
button.click()
time.sleep(1)

button2  = driver.find_element(By.CSS_SELECTOR, "#ui-id-4")
button2.click()
time.sleep(1)

button3  = driver.find_element(By.CSS_SELECTOR, "#ui-id-5")
button3.click()
time.sleep(4)


"hover1 = ActionChains(driver).move_to_element(enabled)"
"hover1.perform()"
"hover2 = ActionChains(driver).move_to_element(enabled)"
"hover2.perform()"
"hover1 = ActionChains(driver).move_to_element(enabled)"
"pdf.click"