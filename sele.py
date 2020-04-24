from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
# driver.maximize_window()
index = driver.implicitly_wait(30000)
try:
    with open("market_trend.csv", "w+") as f:
        driver.get("https://money.cnn.com/data/world_markets/asia/")
        counter = 2
        while counter < 8:
            final_path = f'/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[{counter}]/td[2]/a'.format(counter)
            print(driver.find_element_by_xpath(final_path).click())
            driver.implicitly_wait(30000)
            title = driver.find_element(By.TAG_NAME, "h1")
            print(title.text)
            left = driver.find_element(By.ID, "wsod_quoteLeft")
            print(left.text)
            right = driver.find_element(By.ID, "wsod_quoteRight")
            print(right.text)
            f.write()
            driver.back()
            counter = counter + 1
        driver.get('https://money.cnn.com/data/world_markets/europe/')
        counter = 2
        while counter < 6:
            final_path = f'//*[@id="wsod_indexDataTableGrid"]/tbody/tr[{counter}]/td[2]/a'.format(counter)
            driver.find_element_by_xpath(final_path).click()
            driver.implicitly_wait(30000)
            title = driver.find_element(By.TAG_NAME, "h1")
            print(title.text)
            left = driver.find_element(By.ID, "wsod_quoteLeft")
            print(left.text)
            right = driver.find_element(By.ID, "wsod_quoteRight")
            print(right.text)
            driver.back()
            counter = counter + 1 
        name = driver.get('https://money.cnn.com/data/world_markets/americas/')
        counter = 2
        while counter < 8:
            final_path = f'//*[@id="wsod_indexDataTableGrid"]/tbody/tr[{counter}]/td[2]/a'.format(counter)
            driver.find_element_by_xpath(final_path).click()
            driver.implicitly_wait(30000)
            title = driver.find_element(By.TAG_NAME, "h1")
            print(title.text)
            left = driver.find_element(By.ID, "wsod_quoteLeft")
            print(left.text)
            right = driver.find_element(By.ID, "wsod_quoteRight")
            print(right.text)
            driver.back()
            counter = counter + 1 
        driver.quit()
except:
    print('error')
