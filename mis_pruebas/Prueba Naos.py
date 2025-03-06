"http://naossuite.juntadeandalucia.es/soporte"
import time

from selenium import webdriver  # hay que haber ejecutado `pip install selenium` para que funcione la importación
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

driver = webdriver.Chrome()

try:
    driver.get("http://naossuite.juntadeandalucia.es/soporte")
    "Hacemos el login"

    tbx__user = driver.find_element(By.ID, "staticIdentificacion")
    tbx__user.clear()
    tbx__user.send_keys("mazucena.garcia.ext")
    time.sleep(3)
    driver.save_screenshot("screenshotuser.png")
    tbx__pass = driver.find_element(By.ID, "staticClave")
    tbx__pass.clear()
    tbx__pass.send_keys("Ada_09_2024")
    time.sleep(3)
    driver.save_screenshot("screenshotpass.png")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(3)
    driver.save_screenshot("screenshotlogin.png")
    "Naos desplegamos flecha"

    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#accordion > div > div > div > div > div > div.MuiAutocomplete-endAdornment.css-mxlkbn > button > svg").click()
    time.sleep(3)
    driver.save_screenshot("screenshot2.png")
    "boton Buscar opcion por defecto sin asignar"
    driver.find_element(By.CSS_SELECTOR, "#__next > div.layout > div.MuiContainer-root.MuiContainer-disableGutters.MuiContainer-maxWidthXl > div > div.mb-3.mt-3 > div.MuiGrid-root.search-grid.vertical-space-10.MuiGrid-container > div.MuiGrid-root.search-button.top-space-15.MuiGrid-container.MuiGrid-spacing-xs-1.MuiGrid-item > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-sm-2.MuiGrid-grid-md-2.MuiGrid-grid-lg-2").click()
    time.sleep(3)
    driver.save_screenshot("screenshot3.png")
    "Boton exportar listado en un fichero excel ficheros "

    driver.find_element(By.CSS_SELECTOR, "#__next > div.layout > div.MuiContainer-root.MuiContainer-disableGutters.MuiContainer-maxWidthXl > div > div.mb-3.mt-3 > div.MuiGrid-root.search-grid.vertical-space-10.MuiGrid-container > div.MuiGrid-root.search-button.top-space-15.MuiGrid-container.MuiGrid-spacing-xs-1.MuiGrid-item > div:nth-child(1)").click()
    time.sleep(5)
    driver.save_screenshot("screenshot4.png")
    driver.find_element(By.CSS_SELECTOR, "#formAnular > div > div:nth-child(3)").click()
    time.sleep(5)
    driver.save_screenshot("screenshot5.png")

finally:
     driver.quit()