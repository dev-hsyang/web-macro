from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 1. Navigation 관련 tool

# 1-1. get() : 원하는 페이지로 이동하는 함수
driver.get("https://google.com")
time.sleep(2)
driver.get("https://www.naver.com/")

# 1-2. back() : 뒤로가기
driver.back()
time.sleep(2)

# 1-3. forward() : 앞으로 가기
driver.forward()
time.sleep(2)

# 1-4. refresh() : 새로고침
driver.refresh()
time.sleep(2)
print("Navigation tool done!")


# 2. Website Information 관련 tool

# 2-1. title : 현재 웹페이지의 제목
title = driver.title
print(title, ": 현재 웹페이지의 제목입니다.")

# 2-2. current_url : 현재 웹페이지의 url
url = driver.current_url
print(url, ": 현재 웹페이지의 url입니다.")


# 3. Driver wait 관련 tool

# 3-1. 3초때 로딩이 끝나서, element가 찾아짐
# 3-2. 30초까지는 기다림
# 3-3. 30초 넘어가면 error 발생
try:
    selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        By.CSS_SELECTOR, selector
    ))
except:
    print("exception 발생")
print("Driver wait done! Element is loaded!")