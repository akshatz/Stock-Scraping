import requests
from bs4 import BeautifulSoup

r = requests.get('https://money.cnn.com/data/world_markets/asia/')
soup = BeautifulSoup(r.text, 'html.parser')
resultsRow = soup.find_all("tr")
tr= resultsRow[1:7]
results = []

for resultRow in tr:
    print(resultRow.text)
    try:
        name = resultRow.find('a',{'class':'wsod_symbol'}).text
        country= resultRow.find_all('td')[2].text
        changePct = resultRow.find_all('span',{'stream':'changePct_601823'})[0].find('span',{'class':'posData'}).text
        changeValue = resultRow.find_all('span',{'stream':'change_601823'})[0].find('span',{'class':'posData'}).text
        level =  resultRow.find('span',{'stream':'last_601823'}).text
        last_update = resultRow.find('span',{'stream':'time_601823'}).text
    except:
        continue


results.append({
        'name':name,
        'country': country,
        'changePct': changePct,
        'changeValue': changeValue,
        'level': level,
        'last_update': last_update
    })
