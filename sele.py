# from goto import goto, comefrom, label
from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
driver.get("https://money.cnn.com/data/world_markets/asia/")
# driver.maximize_window()
index = driver.implicitly_wait(30000)
table_row = driver.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[2]/table/tbody')
tr=table_row[0].text
# for index in tr:
#     index.find_element(By.Xpath, 'tr[2]/td[2]').text
driver.quit()
#         title = driver.find_element(By.CLASS_NAME, "wsod_fleft")
#         print(title.text)
#         left = driver.find_element(By.ID, "wsod_quoteLeft").text
#         print(left)
#         right = driver.find_element(By.ID, "wsod_quoteRight").text
#         print(right)
#         n+1
#         driver.back()
#         i = i+1

#         driver.quit()
#     except:
#         print("Error")
