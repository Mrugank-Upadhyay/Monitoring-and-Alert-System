from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

productLink = input("Enter Best Buy Product URL: ")

# we will be using chrome
driver = webdriver.Chrome()
driver.get(productLink)

# We're now going to find the availability tag which is a link tag with an href
availability = driver.find_element(
    By.XPATH, '//link[contains(@href, "http://schema.org")]').get_attribute("href")

if "InStock" in availability:
    # we now have to send ourselves an email notification about the availability
    import alert
    driver.quit()
