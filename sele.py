from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
driver.get("https://money.cnn.com/data/world_markets/asia/")
driver.maximize_window()
print("Maximize")
index = driver.implicitly_wait(30000)

index = driver.find_element(By.CLASS_NAME,'wsod_symbol').click()
print(index)
title = driver.find_element(By.CLASS_NAME, "wsod_fleft")
print(title.text)
left = driver.find_element(By.ID, "wsod_quoteLeft").text
print(left)
right = driver.find_element(By.ID, "wsod_quoteRight").text
print(right)
driver.back()
driver.quit()
index = driver.find_element(By.TAG_NAME,getattr={'href':'/data/world_markets/se_composite'}).click()
print(index.current_url)
driver.quit()