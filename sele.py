from selenium import webdriver 
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome("/home/akshatz/Documents/Python/chromedriver") 
driver.get("localhost:8000/user/akshatzala")
# driver.maximize_window()
# print("Maximize")
index = driver.implicitly_wait(30000)
articles = driver.find_elements_by_class_name("article-title")
print(len(articles))
# /html/body/main/div/div[1]//article[i]/div/h2/a
# /html/body/main/div/div[1]/article[1]/div/h2/a
for i in  range(0,len(articles)+1):
    try:
        if articles[i]:
            articles[i].click()
            driver.back()
            i = i + 1
            print(i)
            # print(i)
            # print("After click")

            # driver.find_element(By.XPATH,"//article[i]/div/h2/a[href]").click()
            # i+1
            # print("After back")
            # print("OUT OF IF")
            driver.quit()
    except:
        pass
        driver.quit()
# for i in  driver.find_elements(By.XPATH("//*[@id='wsod_indexDataTableGrid']/tbody/tr[i]/td[2]./a")).click():
#     try:
#         print(i)
#     title = driver.find_element(By.CLASS_NAME, "wsod_fleft")
#     print(title.te)
#     left = driver.find_element(By.ID, "wsod_quoteLeft").text
#     print(left)
#     right = driver.find_element(By.ID, "wsod_quoteRight").text
#     print(right)
#     n+1
#     driver.back()
# # //*[@id="wsod_indexDataTableGrid"]/tbody/tr[2]/td[2]/a

# driver.quit()
#     except:
#         print("Error")
