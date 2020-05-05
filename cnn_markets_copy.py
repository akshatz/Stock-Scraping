import os
os.system("")
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
from datetime import datetime
now = datetime.utcnow()
now_date = now.strftime("%Y/%m/%d")
now_time = now.strftime("%H:%M:%S")
print(now_time)
driver = webdriver.Chrome() 
# driver.maximize_window()
index = driver.implicitly_wait(30000)
file = 'market_trend_copy.csv'
file_exists = os.stat(file).st_size == 0
def stockScraping():
    with open("market_trend_copy.csv","a") as f:
        try:
            header = "Date, Time, Index, Previous close, Day Open, Day High, Day Low, LTP/Closing Prices\n"
            if file_exists:
                f.write(header)
            if "02:30:00" < now_time and now_time < "03:30:00":
                driver.get("https://money.cnn.com/data/world_markets/asia/")
                counter = 2
                print()
                while counter < 4:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+now_time+","+driver.find_element_by_xpath(final_path).text+",")
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:4]+"."+price[4:6]+"," +price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:25]+","+ltp+"\n")
                    driver.back()
                    counter = counter + 1
                while counter < 8:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+now.strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:]+","+ltp+"\n")
                    driver.back()
                    counter = counter + 1
                driver.quit()
                print(style.GREEN + "Successfully run the program for Asian Stock Market")
            elif "04:29:00" < now_time < "04:31:00":
                counter = 2
                driver.get("https://money.cnn.com/data/world_markets/europe/")
                while counter < 8:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+now.strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string = left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')            
                    f.write(price[0:4]+"."+price[4:6]+"," +price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:]+","+ltp+"\n")
                    driver.back()
                    counter = counter +2
                counter = 3
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now_date+","+now.strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                driver.find_element_by_xpath(final_path).click()
                driver.implicitly_wait(30000)
                title = driver.find_element(By.TAG_NAME, "h1")
                left = driver.find_element(By.ID, "wsod_quoteLeft")
                price = []
                string = left.text
                for k in string:
                    if k.isdigit() == True:
                        price.append(k)
                price = ''.join(price)
                ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                ltp = ltp.replace(",", '')  
                f.write(price[0:3]+"."+price[3:5]+"," +price[5:8]+"."+price[8:10]+","+price[10:13]+"."+price[13:15]+","+price[15:18]+"."+price[18:20]+","+ltp+"\n")
                driver.back()
                counter = 5
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now_date+","+now.strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                driver.find_element_by_xpath(final_path).click()
                driver.implicitly_wait(30000)
                title = driver.find_element(By.TAG_NAME, "h1")
                left = driver.find_element(By.ID, "wsod_quoteLeft")
                price = []
                string = left.text
                for k in string:
                    if k.isdigit() == True:
                        price.append(k)
                price = ''.join(price)
                ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                ltp = ltp.replace(",", '')    
                f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:]+","+ltp+"\n")
                driver.back()    
                driver.quit()
                print(style.GREEN + "Successfully run the program for European Stock Market")
            elif "12:00:00" < now_time < "12:01:00":
                driver.get('https://money.cnn.com/data/world_markets/americas/')
                counter = 2
                while counter <  5:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:]+","+ltp+"\n")
                    counter = counter + 2
                    driver.back()
                while counter < 7:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:4]+"."+price[4:6]+","+price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:]+","+ltp+"\n")
                    counter = counter + 3
                    driver.back()
                counter = 3
                while counter < 8:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:4]+"."+price[4:6]+"," +price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:]+","+ltp+"\n")
                    driver.back()
                    counter = counter + 3
                    break
                counter = 7
                while counter < 5:
                    final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                    f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                    driver.find_element_by_xpath(final_path).click()
                    driver.implicitly_wait(30000)
                    title = driver.find_element(By.TAG_NAME, "h1")
                    left = driver.find_element(By.ID, "wsod_quoteLeft")
                    price = []
                    string= left.text
                    for k in string:
                        if k.isdigit() == True:
                            price.append(k)
                    price = ''.join(price)
                    ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                    ltp = ltp.replace(",", '')
                    f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:]+","+ltp+"\n")
                    driver.back()
                    counter = counter + 1
                counter = 5
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                driver.find_element_by_xpath(final_path).click()
                driver.implicitly_wait(30000)
                title = driver.find_element(By.TAG_NAME, "h1")
                left = driver.find_element(By.ID, "wsod_quoteLeft")
                price = []
                string= left.text
                for k in string:
                    if k.isdigit() == True:
                        price.append(k)
                price = ''.join(price)
                ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                ltp = ltp.replace(",", '')    
                f.write(price[0:3]+"."+price[3:5]+"," +price[5:8]+"."+price[8:10]+","+price[10:13]+"."+price[13:15]+","+price[15:18]+"."+price[18:]+","+ltp+"\n")
                driver.back()
                counter = 7
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now_date+","+datetime.utcnow().strftime("%H:%M:%S")+","+driver.find_element_by_xpath(final_path).text+",")
                driver.find_element_by_xpath(final_path).click()
                driver.implicitly_wait(30000)
                title = driver.find_element(By.TAG_NAME, "h1")
                left = driver.find_element(By.ID, "wsod_quoteLeft")
                price = []
                string= left.text
                for k in string:
                    if k.isdigit() == True:
                        price.append(k)
                price = ''.join(price)
                ltp = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr/td[1]/span").text
                ltp = ltp.replace(",", '')    
                f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:]+","+ltp+"\n")
                driver.quit()
                print(style.GREEN + "Successfully run the program for american stock market")
            else: 
                f.close()
                driver.quit()
                print(style.RED+"Cannot run the file")
        except:
            driver.quit()
            print(style.RED+ 'error')

import datetime as dt 
d = dt.date.today()
d = d.weekday()
if d < 6:
    stockScraping()
else:
    print("Error")