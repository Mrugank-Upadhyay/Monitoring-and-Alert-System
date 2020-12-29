from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

productLink = input("Enter Best Buy Product URL: ")

# we will be using chrome
driver = webdriver.Chrome("/usr/bin/chromedriver")


# throw away email client id
# 1070153309962-2t8u0k6gj53jl9k8rfmnr2lq5aq40t72.apps.googleusercontent.com

# client secret
# oy0SDoAkyqspfs05zFweddfn

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
    import alert

driver.quit()
