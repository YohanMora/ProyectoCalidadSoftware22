from lib2to3.pgen2 import driver
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get ("https://www.rescatewildlife.org/es/inicio/")