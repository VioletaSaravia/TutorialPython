"""
Día 14: Selenium Test

Instagram ya no permite ver perfiles sin cuenta. RIP :(

Update 21/06: ahora funciona
"""
# WAITS: https://selenium-python.readthedocs.io/waits.html

# import selenium
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
#chrome_options.add_argument('-headless')
chrome_options.add_argument('-width=1920')
chrome_options.add_argument('-height=1080')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

xpaths_ig = {}
xpaths_ig['Posts'] = '/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span'
xpaths_ig['Seguidores'] = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
xpaths_ig['Siguiendo'] = '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span'

login = {}
login['username'] = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
login['password'] = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
login['boton'] = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div'

Users = {}
Users['Hunter Schafer'] = 'hunterschafer'

def url_ig(user):
    """ Convierte user en url de ig """
    return 'https://www.instagram.com/{}/?hl=en'.format(user)

def cargar(xpath):
    """ carga xpath """
    return driver.find_element_by_xpath(xpath).text

def cargar2(xpath):
    """ carga xpath """
    return driver.find_element_by_xpath(xpath)

tu_user = input("Ingrese nombre de usuario: ")
tu_pass = getpass("Ingrese contraseña: ")
# tu_pass = ''
# tu_user = 'estro.yonqui'

driver.get("https://www.instagram.com/?hl=en")
breakpoint()
WebDriverWait(driver, 30)
login_link = cargar2(login['username'])
login_link.click()
login_link.send_keys(tu_user)
pass_link = cargar2(login['password'])
pass_link.click()
pass_link.send_keys(tu_pass)
cargar2(login['boton']).click()
WebDriverWait(driver, 10)

for nombre, username in Users.items():
    driver.get(url_ig(username))
    WebDriverWait(driver, 30)
    breakpoint()
    for stat, valor in xpaths_ig.items():
        print(cargar(valor))