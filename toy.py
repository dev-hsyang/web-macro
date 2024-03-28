from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 1. 웹 브라우저 주소창 컨트롤 driver.get
url = "https://www.naver.com/"
driver.get(url)
time.sleep(3)

# 2-1. 요소 찾아서 copy (실제 웹 + 개발자 tool)
css_selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg"

# 2-2. 찾아온 요소를 driver.find_element로 가져와서 변수에 저장
group = driver.find_element(By.CSS_SELECTOR, css_selector)

# 3. 데이터 가져오기
print(group.text)
time.sleep(5)