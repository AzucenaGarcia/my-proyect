
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tables")

def get(fila, columna):
    celda = driver.find_element(By.CSS_SELECTOR, f"#table1 > tbody > tr:nth-child({fila}) > td:nth-child({columna})")
    return celda


print(get(1,1).text)

