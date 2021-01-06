# Monitoring-and-Alert-System

Best Buy hasn't implemented an alert system for their out-of-stock products yet unlike Newegg or B&H. While finding parts for my PC build, I need to be notified when parts have been restocked. I thought to make this script to automate the process.

The script takes a list of urls from a text file and for each product, scrapes availability information from the specified Best Buy webpage and if it finds the product to be in stock, it will notify me via email. I used Selenium to automate the webscraping using its chrome webdriver (with a headless implementation) and element searching; then incorporated SMTPlib to send emails to a gmail account securely using SMTPSSL.

The task scheduling is done using Cron jobs on Linux and Windows Task Scheduler on Windows.

Considering many online stores don't have alert systems, I might create separate webscraping scripts for them and then roll everything into a single script. That way, it can simply analyze the url to identify which script to use and I can get a general alert system going, and I'd only need my single wishlist.txt to stay organized!
