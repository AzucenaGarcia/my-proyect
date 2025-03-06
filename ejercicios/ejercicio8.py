
""" Crear un metodo que reciba dos parametros booleanos
""y que  dejee el estado final igual en la pgagina https://the-internet.herokuapp.com/checkboxes"""


"https://the-internet.herokuapp.com/login logar y sacar captura de pantalla"

from selenium import webdriver  # hay que haber ejecutado `pip install selenium` para que funcione la importación
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

print(driver.title)
assert "hellow" in driver.title

tbx__user = driver.find_element(By.ID, "username")
tbx__user.clear()
tbx__user.send_keys("tomsmith")

tbx__pass = driver.find_element(By.ID, "password")
tbx__pass.clear()
tbx__pass.send_keys("SuperSecretPassword!")



def marcar_checkboxes(chk1, chk2):

marcar_checkboxes(chk1, chk2):