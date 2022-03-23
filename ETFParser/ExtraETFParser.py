from unittest import TestResult
import requests
from bs4 import BeautifulSoup
from lxml import etree

#URL
BaseURL = "https://extraetf.com/etf-profile/"

#xpaths for parsing from HTML
Title_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[1]/h1'
ISIN_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[2]/span[1]'
WKN_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[2]/span[2]'
Ticker_xpath = '/html/body/app-root/app-page-template/div[1]/div/app-etf-profile/div[1]/div[1]/div[1]/div/div[2]/span[3]'
Price_xpath = '//*[@id="overview"]/app-tab-overview/div/div[1]/div[1]/div/div/app-real-time-course/span/span'
OneWeekPerf_xpath = '//*[@id="overview"]/app-tab-overview/div/div[2]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]/span/span'
OneMonthPerf_xpath = '//*[@id="overview"]/app-tab-overview/div/div[2]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/span/span'
YTDPerf_xpath = '//*[@id="overview"]/app-tab-overview/div/div[2]/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/span'
FondsSize_xpath = '//*[@id="overview"]/app-tab-overview/div/div[1]/div[2]/div[2]/div/table/tbody/tr[5]/td[2]'

class ExtraetfETF:

    def __init__(self, id) -> None:
        self.id = id
        self.Title = ""
        self.ISIN = ""
        self.WKN = ""
        self.Ticker = ""
        self.Price = ""

        #Performance Information
        self.OneWeekPerf = ""
        self.OneMonthPerf = ""
        self.YTDPerf = ""
        self.FondsSize = ""

        #URL
        self.ParseURL = BaseURL+self.id

    def parse(self) -> None:
        html_text = requests.get(self.ParseURL).text
        soup = BeautifulSoup(html_text, 'html.parser')

        #Create DOM-Object for parsing
        dom = etree.HTML(str(soup))

        #Parse and Write Information
        #Basic Information
        self.id = id
        self.Title = dom.xpath(Title_xpath)[0].text[1:] #durch [1:] wird das führende Leerzeichen abgeschnitten
        self.ISIN = dom.xpath(ISIN_xpath)[0].text.split(" ")[2]
        self.WKN = dom.xpath(WKN_xpath)[0].text.split(" ")[2]
        self.Ticker = dom.xpath(Ticker_xpath)[0].text.split(" ")[2]
        self.Price = dom.xpath(Price_xpath)[0].text

        #Performance Information
        self.OneWeekPerf = dom.xpath(OneWeekPerf_xpath)[0].text
        self.OneMonthPerf = dom.xpath(OneMonthPerf_xpath)[0].text
        self.YTDPerf = dom.xpath(YTDPerf_xpath)[0].text
        self.FondsSize = dom.xpath(FondsSize_xpath)[0].text

    def CreateDict(self):
        x = dict(
            ID = self.id,
            Title = self.Title,
            ISIN = self.ISIN,
            WKN = self.WKN,
            Ticker = self.Ticker,
            Price = self.Price,
            OneWeekPerf = self.OneWeekPerf,
            OneMonthPerf = self.OneMonthPerf,
            YTDPerf = self.YTDPerf,
            FondsSize = self.FondsSize,
            ParseURL = self.ParseURL
        )

        return x
    
    def CreateString(self):
        data = self.CreateDict()
        string = ""

        for key in data:
            string += str(key) + ": " + str(data[key])
            string += "\n"
        return string

    def print(self) -> None:
        print(self.Title)
        print("---------------------------------------")
        print("ISIN:\t\t\t", self.ISIN)
        print("WKN:\t\t\t", self.WKN)
        print("Ticker:\t\t\t", self.Ticker)
        print("Price:\t\t\t", self.Price)
        print("Fonds Size:\t\t", self.FondsSize)

        #Performance Information
        
        print("Performance:")
        print("1 Week:\t\t\t", self.OneWeekPerf)
        print("1 Month:\t\t", self.OneMonthPerf)
        print("YTD:\t\t\t", self.YTDPerf)
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
