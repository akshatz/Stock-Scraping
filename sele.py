from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
driver.get("https://money.cnn.com/data/world_markets/asia/")
# driver.maximize_window()
index = driver.implicitly_wait(30000)
row_size = len(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody/tr'))-1
n = row_size
print(n)
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
    driver.back()
    counter = counter + 1
driver.quit()   
