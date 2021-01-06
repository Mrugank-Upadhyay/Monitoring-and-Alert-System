from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

productLink = ""


def webscrape(link):
    productLink = link
    print(productLink)
    # we will be using a headless implementation of chrome
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)
    driver.get(productLink)

    # We're now going to find the availability tag which is a link tag with an href
    availability = driver.find_element(
        By.XPATH, '//link[contains(@href, "http://schema.org")]').get_attribute("href")

    if "InStock" in availability:
        # we now have to send ourselves an email notification about the availability
        exec(open("/home/mrugank/Documents/Python Projects/Monitoring-and-Alert-System/alert.py", "r").read())
        driver.quit()


def main():
    with open("/home/mrugank/Documents/Python Projects/Monitoring-and-Alert-System/Monitor.txt", 'r') as monitorFile:
        lines = monitorFile.readlines()
        regSearch = re.compile(r'https://www.bestbuy.c(a|om)(\S)+(\s)?')
        for line in lines:
            urlMatch = regSearch.search(line)
            url = urlMatch.group(0) if urlMatch else None
            if url is not None:
                processedUrl = re.sub(
                    '^(.*)(?=https://www.bestbuy.c(a|om))', "", url)
                webscrape(processedUrl)


if __name__ == '__main__':
    main()
