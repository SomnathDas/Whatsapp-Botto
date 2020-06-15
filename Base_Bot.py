from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import parser


PATH = "/home/somnathdas/Whatsapp-Botto/geckodriver" #Add Your own executable path of web driver

driver = webdriver.Firefox(executable_path=PATH) ##Add Your own executable path of web driver

#Bot will open the site
driver.get("https://web.whatsapp.com")

# Message that user wants to send
#text_message = input("Enter the text message:\n")
text_message = "/Bot testing/"

#Group Or Contact Name to send message
#Namae = input("Enter the name of contact or group:\n")
Namae = "Otaku Hub"

#Printing Instructions
#print("!! Scan The QR Code in the opened window !! \n ")
#We will add instruction on our own!!!!!!!! LATER

#Bot will wait for user to scan the QR code
try:
    element = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"))
    )
except:
    print("Timeout")
    driver.quit()

#Bot will do some shits
search = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
search.send_keys(Namae)

#so basically, this code below clicks on the topmost search result so the name we type is case-sensitive XD
search.send_keys(Keys.RETURN)

#driver.find_element_by_name("Otaku Hub").click()
msg = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
msg.click() 
msg.send_keys(text_message)
msg.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
url = driver.page_source	
soup = bs(url, "lxml")
driver.implicitly_wait(14)
getText = soup.find_all("span", class_="_3Whw5 selectable-text invisible-space copyable-text")
print(getText)