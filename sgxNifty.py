import re
import requests
from bs4 import BeautifulSoup
# import responses
# regex=re.findall("^indexes rates (?=positive|negative))\\w+$", indexes.rates)

r = requests.get('https://sgxnifty.org/world-markets/')
# print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

resultsRow = soup.find_all("table")[0]
headers = "Symbol, Close, High, Low, Last Trade\n"
f =open("marketTrendSGXNifty.csv", "a+")
# close = results.getText("td",{"class": "indexes-rates.positve"})[0]
f.close()
with open("market_trend_sgx_nifty.csv", "a+") as f:
    headers = "Symbol, Close, High, Low, Last Trade\n"
    f.write(headers)
    for result in resultsRow:
        try:
                symbol = result.find("td",{"class":"indexes-name"}).text
                close = result.getText("td",{"class": "indexes-rates.positve"})
                date = result.find("td",{"class":"indexes-date"}).text
                f.write(symbol+","+","+","+","+date+"\n")
        except:
            print("End")