from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# we will be using chrome
# driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
# try:
driver.get("https://www.bestbuy.ca/en-ca/product/asus-tuf-24-fhd-144hz-1ms-gtg-ips-led-freesync-gaming-monitor-vg249q-black/14405119")
# productPriceContainer = driver.find_element_by_class_name(
#     "productPricingContainer_3gTS3")
# print(productPriceContainer.text)
availability = driver.find_element(
    By.XPATH, "//link[contains(@href, 'http://schema.org')]").value_of_css_property('href')
print(availability)
# except:
#     pass
driver.quit()
