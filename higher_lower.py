"""
Día 14: Selenium Test
"""

import selenium
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/hunterschafer/?hl=en')

POSTS_XPATH = 'html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span'
SEGUIDORES_XPATH = 'html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
SIGUIENDO_XPATH = '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span'

Posts = driver.find_element_by_xpath(POSTS_XPATH).text
Seguidores = driver.find_element_by_xpath(SEGUIDORES_XPATH).text
Siguiendo = driver.find_element_by_xpath(SIGUIENDO_XPATH).text

print(Posts)
print(Seguidores)
print(Siguiendo)
# /html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span
# /html/body/div[1]/section/main/div/ul/li[2]/a/span
# /html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span
# /html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span
