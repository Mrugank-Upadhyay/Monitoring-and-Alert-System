from selenium import webdriver
from bs4 import BeautifulSoup

# we will be using chrome
# driver = webdriver.Chrome("/usr/bin/chromedriver")
driver = webdriver.Chrome()
driver.get("https://www.bestbuy.ca/en-ca/product/asus-tuf-24-fhd-144hz-1ms-gtg-ips-led-freesync-gaming-monitor-vg249q-black/14405119")
priceContainer = driver.find_element_by_class_name("pricingContainer_25k3c")
driver.quit()
