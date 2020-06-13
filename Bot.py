from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/home/somnathdas/Whatsapp-Botto/geckodriver" #Add Your own executable path of web driver

driver = webdriver.Firefox(executable_path=PATH) ##Add Your own executable path of web driver

#Bot will open the site
driver.get("https://web.whatsapp.com")

#Bot will print out the login instructions by finding it on start page
#instructions = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]")
#print(instructions.text)
#We will add instruction on our own!!!!!!!! LATER

#Bot will wait for user to scan the QR code
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"))
    )
except:
    driver.quit()

#Bot will do some shits
search = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
search.send_keys("Otaku Hub")
#so basically, this code below clicks on the topmost search result so the name we type is case-sensitive XD
search.send_keys(Keys.RETURN)
#driver.find_element_by_name("Otaku Hub").click()
msg = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
msg.click() 
msg.send_keys("Hello World")
msg.send_keys(Keys.RETURN)
print("Complete")


