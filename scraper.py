import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from constants import LEADERBORD_URL
from selenium.webdriver.common.by import By
from helper import click_load_more,scroll_to_last
import time

chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    options=chrome_options
)
driver.get(LEADERBORD_URL)
driver.maximize_window()
# to get all the data 
click_load_more(driver)
time.sleep(5)
scroll_to_last(driver)

time.sleep(10)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
ul_elements = soup.find_all("ul",class_ = "km-list")
lis = ul_elements[2].find_all("li")
for li in lis:
    print(li.text)
driver.quit()


