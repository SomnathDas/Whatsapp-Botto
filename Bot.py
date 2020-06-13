from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

PATH = "/home/somnathdas/Whatsapp-Botto/geckodriver" #Add Your own executable path of web driver

driver = webdriver.Firefox(executable_path=PATH) ##Add Your own executable path of web driver

driver.get("https://web.whatsapp.com")
print("Website Loading Complete, now quitting")
driver.quit()