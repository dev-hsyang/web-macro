from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = "https://www.naver.com/"
driver.get(url)
time.sleep(3)

css_selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg"
group = driver.find_element(By.CSS_SELECTOR, css_selector)
print(group.text)
time.sleep(5)