import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
from datetime import datetime
now = (datetime.now())
now = now.strftime("%Y/%m/%d,%H:%M:%S")
driver = webdriver.Chrome() 
index = driver.implicitly_wait(30000)
file = 'market_trend.csv'
file_exists = os.stat(file).st_size == 0
with open("market_trend.csv","a") as f:
    try:
        header = "Date, Time, Index, Previous close, Day Open, Day High, Day Low, LTP/Closing Prices\n"
        if file_exists:
            f.write(header)
        if now > "07:59:00" and  not now > "08:01:00":
            driver.get("https://money.cnn.com/data/world_markets/asia/")
            counter = 2
            while counter < 4:
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
        elif now > "11:00:00" and not now  > "11:05:00":
            counter = 2
            driver.get("https://money.cnn.com/data/world_markets/europe/")
            while counter < 8:
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
            f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
            f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
        elif now > "18:00:00": #and not now > "18:05:01":
            driver.get('https://money.cnn.com/data/world_markets/americas/')
            counter = 2
            while counter <  5:
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
                counter = counter + 2
            while counter < 7:
                final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
                f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
            f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
            f.write(now+","+driver.find_element_by_xpath(final_path).text+",")
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
        else:
            f.close()
            print("Cannot run the file")
            driver.quit()
    except:
        driver.quit()
        print('error')