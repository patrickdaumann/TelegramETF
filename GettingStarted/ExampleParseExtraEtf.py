import requests
from bs4 import BeautifulSoup
from lxml import etree

BaseURL = "https://extraetf.com/etf-profile/"
TestISIN = "LU1829221024"
FullURL = BaseURL+TestISIN

#HTML per Request ziehen und Soup object erstellen
html_text = requests.get(FullURL).text
soup = BeautifulSoup(html_text, 'html.parser')

#DOM Erstellen
dom = etree.HTML(str(soup))

#xpath des Preises auf extraetf
Title_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[1]/h1'
Price_xpath = '//*[@id="overview"]/app-tab-overview/div/div[1]/div[1]/div/div/app-real-time-course/span/span'

print("ETF:", dom.xpath(Title_xpath)[0].text)
print("Kurs:", dom.xpath(Price_xpath)[0].text)


