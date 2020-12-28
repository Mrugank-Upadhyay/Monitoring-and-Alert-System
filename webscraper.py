from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time

# we will be using chrome
# driver = webdriver.Chrome("/usr/bin/chromedriver")
tempLink = "https://www.bestbuy.ca/en-ca/product/asus-tuf-24-fhd-144hz-1ms-gtg-ips-led-freesync-gaming-monitor-vg249q-black/14405119"


link = input("Enter input Link: ")
driver = webdriver.Chrome()
driver.get(link)

# We're now going to find the availability tag which is a link tag with an href
availability = driver.find_element(
    By.XPATH, '//link[contains(@href, "http://schema.org")]').get_attribute("href")

if "InStock" in availability:
    # we now have to send ourselves an email notification about the availability
    print("I'm in stock!")

elif "OutOfStock" in availability:
    print("Whoops, I'm out of stock!")

driver.quit()
