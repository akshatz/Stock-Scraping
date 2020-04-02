import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

r = requests.get('https://money.cnn.com/data/world_markets/asia/')
# driver = webdriver.Chrome(executable_path='/home/akshatz/Documents/Python/chromedriver')
# driver.get('https://money.cnn.com/data/world_markets/asia/')
# driver.maximize_window()
soup = BeautifulSoup(r.text, 'html.parser')
resultsRow = soup.find_all("tr")
tr= resultsRow[1:8]
results = []

# print(tr[0])
# print(header)
# results = []
# changeValue = resultsRow.getText('span', {'stream':'change_601823'})
# print(changeValue)
# name = None
# del(name,changePct, changeValue, level, last_update)
# f= open("market_trend.csv","w")
# header = "Index, Country, ChangedPercentage, ChangedValue, Last Updated"
# # f.write(header)
# f.close()
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
    # country = resultRow.find('td').text
    # # print(country)
    # changePct = resultRow.find_all('span',{'stream':'changePct_601823'})[0].find('span',{'class':'posData'}).text
    # changeValue = resultRow.find_all('span',{'stream':'change_601823'})[0].find('span',{'class':'posData'}).text
    # level = resultRow.find('span',{'stream':'last_601823'}).text
    # last_update = resultRow.find('span',{'stream':'time_601823'}).text
    # print(country, changePct, changeValue, level, last_update)
    # # except:
    #     continue
    # with open('market_trend.csv', 'a'):
    #     f.write(name+','+changeValue+','+changePct+','+level+','+ last_update+','+'\t \n')
# index = driver.implicitly_wait(30000)
# index = driver.find_element(By.CLASS_NAME,'wsod_symbol').click()
# print(index)
# f.open("market_trend.csv", "w")
# print(header)
# with open("market_trend.csv", "w" )as rf:
# title = driver.find_element(By.CLASS_NAME, "wsod_fleft")
# print(title.text)
# left = driver.find_element(By.ID, "wsod_quoteLeft").text
# print(left)
# right = driver.find_element(By.ID, "wsod_quoteRight").text
# print(right)
# driver.back()
# driver.quit()
# index = driver.find_element(By.TAG_NAME,getattr={'href':'/data/world_markets/se_composite'}).click()
# print(index.current_url)


results.append({
        'name':name,
        'country': country,
        'changePct': changePct,
        'changeValue': changeValue,
        'level': level,
        'last_update': last_update
    })

print(results)
# name = resultsRow[1].find_all('span',{'stream':'changePct_601823'})[0].find('span',{'class':'posData'}).text
# print(name)