# Monitoring-and-Alert-System

Best Buy hasn't implemented an alert system for their out-of-stock products yet unlike Newegg or B&H. While finding parts for my PC build, I need to be notified when parts have been restocked. I thought to make this script to automate the process.

The script will first scrape availability information from the specified Best Buy webpage and if it finds the product to be in stock, it will notify me via email. I'm going to improve this to work on a list of products taken from a text file and use AutoHotKey to have the script run multiple times throughout the day. The issue is since PC Parts tend to sell out quick, multiple daily checks help ensure I have a good chance at buying them before they sell out!

I used Selenium to automate the webscraping using its chrome webdriver and element searching; then incorporated SMTPlib to send emails to a gmail account securely using SMTPSSL.
