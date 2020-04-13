from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
# driver.maximize_window()
index = driver.implicitly_wait(30000)
with open("market_trend.csv","a+") as f:
    headers = "Index, Previous close, Day High, Day open, Day close\n"
    f.write(headers)
    try:
        driver.get("https://money.cnn.com/data/world_markets/asia/")
        counter = 2
        while counter < 4:
            final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
            f.write(driver.find_element_by_xpath(final_path).text+",")
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
            f.write(price[0:4]+"."+price[4:6]+"," +price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:24]+"\n")
            driver.back()
            counter = counter + 1    
        print(counter)    
        while counter < 8:
            final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
            f.write(driver.find_element_by_xpath(final_path).text+",")
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
            # print(price)
            f.write(price[0:5]+"."+price[5:7]+"," +price[7:12]+"."+price[12:14]+","+price[14:19]+"."+price[19:21]+","+price[21:26]+"."+price[26:28]+"\n")
            driver.back()
            counter = counter + 1    
        
        # driver.get("https://money.cnn.com/data/world_markets/europe/")
        # if counter == 2 | counter == 4 | counter == 6:
        #     final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
        #     f.write(driver.find_element_by_xpath(final_path).text+",")
        #     driver.find_element_by_xpath(final_path).click()
        #     driver.implicitly_wait(30000)
        #     title = driver.find_element(By.TAG_NAME, "h1")
        #     left = driver.find_element(By.ID, "wsod_quoteLeft")
        #     price = []
        #     string = left.text
        #     for k in string:
        #         if k.isdigit() == True:
        #             price.append(k)
        #     price = ''.join(price)
        #     print(price)
        #     f.write(price[0:6]+"."+price[6:8]+"," +price[8:16]+"."+price[16:20]+","+price[20:26]+"."+price[26:32]+","+price[18:22]+"."+price[22:24]+"\n")
        # elif counter == 3: 
        #     pass
        # driver.get('https://money.cnn.com/data/world_markets/americas/')
        # counter = 2
        # while counter < 8:
        #     final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
        #     f.write(driver.find_element_by_xpath(final_path).text+",")
        #     driver.find_element_by_xpath(final_path).click()
        #     driver.implicitly_wait(30000)
        #     title = driver.find_element(By.TAG_NAME, "h1")
        #     left = driver.find_element(By.ID, "wsod_quoteLeft")
        #     price = []
        #     string= left.text
        #     for k in string:
        #         if k.isdigit() == True:
        #             price.append(k)
        #     price = ''.join(price)
        #     f.write(price[0:4]+"."+price[4:6]+"," +price[6:10]+"."+price[10:12]+","+price[12:16]+"."+price[16:18]+","+price[18:22]+"."+price[22:24]+"\n")
        #     driver.back()
        #     counter = counter + 1    
        f.close()
        driver.quit()
    except:
        print('error')
