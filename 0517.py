#0517
#pip install beautifulsoup4

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

'''
#(1) news를 가져온다.
driver.get("https://www.naver.com/")
time.sleep(3)

#(2) 원하는 버튼을 누르는 명령을 한다. 뉴스 버튼 누름
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)

newstitle1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle1)

newstitle2 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[4]/a/div[2]/div").text
print(newstitle2)
'''
'''
#(3) 아파트 가격 알아보기
driver.get("https://new.land.naver.com/search/")
driver.find_element(By.XPATH,"/html/body/div[2]/div/header/div[1]/form/fieldset/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/header/div[1]/form/fieldset/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/header/div[1]/form/fieldset/button[1]").click()
time.sleep(1)
#전세값 가져오기
rentprice1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[2]/dd").text
print(rentprice1)
time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[2]/div/header/div[1]/form/fieldset/div/input").send_keys("망원동 우림")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/header/div[1]/form/fieldset/button[1]").click()
time.sleep(1)
#매매값 가져오기
rentprice2 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[1]/dd").text
print(rentprice2)
time.sleep(1)
'''
#(4) 주식 가져오기
driver.get("https://finance.naver.com/")

subject1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
time.sleep(1)
subject2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
time.sleep(1)
subject3 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text
time.sleep(1)
print(subject1,subject2,subject3)
print("=============================")
lst = []
for i in range(10) :
    subject = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
    lst.append(subject)

print(lst)
'''
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent" : "Dongyang Mirea Univ"
}

webpage = requests.get("https://sports.news.naver.com/news.nhn?oid=236&aid=0000233899", headers=headers)
print(webpage)
#print(webpage.content)
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)

news = soup.select_one("#container").get_text().strip()
print(news)
'''