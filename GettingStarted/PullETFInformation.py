import requests
from bs4 import BeautifulSoup
from lxml import etree

def PullETFInfo(ETFISIN):
    #Define Xpaths for Parsing
    Title_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[1]/h1'
    Price_xpath = '//*[@id="overview"]/app-tab-overview/div/div[1]/div[1]/div/div/app-real-time-course/span/span'
    
    #Define URLS
    BaseURL = "https://extraetf.com/etf-profile/"
    FullURL = BaseURL+ETFISIN

    #Pull Information from ExtraETF.com
    html_text = requests.get(FullURL).text
    soup = BeautifulSoup(html_text, 'html.parser')

    #Create DOM-Object for parsing
    dom = etree.HTML(str(soup))

    print("-------------------------------------------")
    print("ETF:", dom.xpath(Title_xpath)[0].text)
    print("Kurs:", dom.xpath(Price_xpath)[0].text)
    print("-------------------------------------------")


TestISINs = ["LU1829221024", "IE00B1FZS350", "IE00B0M62Q58"]

for TestISIN in TestISINs:
    PullETFInfo(TestISIN)
