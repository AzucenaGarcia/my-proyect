"https://the-internet.herokuapp.com/login logar y sacar captura de pantalla"

from selenium import webdriver  # hay que haber ejecutado `pip install selenium` para que funcione la importación
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    "print(driver.title)"
    "assert ""hellow" "in driver.title"

    tbx__user = driver.find_element(By.ID, "username")
    tbx__user.clear()
    tbx__user.send_keys("tomsmith")

    tbx__pass = driver.find_element(By.ID, "password")
    tbx__pass.clear()
    tbx__pass.send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button").click()
    driver.save_screenshot("screenshot.png")
finally:
     driver.quit()

