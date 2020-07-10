from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
import parser
import os
import configparser
from selenium.common.exceptions import NoSuchElementException
from subprocess import call  

Firefox_PATH = "/home/somnath/Whatsapp-Botto/geckodriver" #Add Your own executable path of web driver
Chrome_PATH = "/home/somnath/Whatsapp-Botto/chromedriver"

#driver = webdriver.Chrome(Chrome_PATH) #This is for chrome web driver!!
driver = webdriver.Firefox(executable_path=Firefox_PATH) ##Add Your own executable path of web driver

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


def read_last_in_message(driver):
    """
    Reading the last message that you got in from the chatter
    """
    for messages in driver.find_elements_by_xpath("//div[contains(@class,'message-in')]"):
        try:
            message = ""
            emojis = []

            message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")

            message = message_container.find_element_by_xpath(".//span[contains(@class,'selectable-text invisible-space copyable-text')]").text

            for emoji in message_container.find_elements_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]"):
                emojis.append(emoji.get_attribute("data-plain-text"))

        except NoSuchElementException:  # In case there are only emojis in the message
            try:
                message = ""
                emojis = []
                message_container = messages.find_element_by_xpath(".//div[@class='copyable-text']")

                for emoji in message_container.find_elements_by_xpath(".//img[contains(@class,'selectable-text invisible-space copyable-text')]"):
                    emojis.append(emoji.get_attribute("data-plain-text"))
            except NoSuchElementException:
                pass

    return message, emojis

def main():
    previous_in_message = None
    while True:
        last_in_message, emojis = read_last_in_message(driver)

        if previous_in_message != last_in_message:
            print(last_in_message, emojis)
            previous_in_message = last_in_message

            time.sleep(1)

main()

#url = driver.page_source	
#soup = bs(url, "lxml")
#driver.implicitly_wait(14)

#div = []
#text = []

#div = soup.find_all("div", { "class" : "eRacY" })
#print(div)
#text = div.find("span", {"class" : "selectable-text invisible-space copyable-text"})
#print(text)

