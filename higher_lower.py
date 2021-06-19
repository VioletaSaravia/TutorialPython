"""
Día 14: Selenium Test

Instagram ya no permite ver perfiles sin cuenta. Esto no funciona más. RIP :(
(hasta que aprenda de OAuth al menos)
"""

# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('-headless')
chrome_options.add_argument('-width=1920')
chrome_options.add_argument('-height=1080')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

xpaths_ig = {}
xpaths_ig['Posts'] = '/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span'
xpaths_ig['Seguidores'] = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
xpaths_ig['Siguiendo'] = '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span'

Users = {}
Users['Hunter Schafer'] = 'hunterschafer'

def url_ig(user):
    """ Convierte user en url de ig """
    return 'https://www.instagram.com/{}/?hl=en'.format(user)

def cargar(xpath):
    """ carga xpath """
    return driver.find_element_by_xpath(xpath).text

for nombre, username in Users.items():
    driver.get(url_ig(username))
    # breakpoint()
    for stat, valor in xpaths_ig.items():
        print(cargar(valor))
