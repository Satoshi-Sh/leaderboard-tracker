import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from constants import LEADERBOARD_URL
from selenium.webdriver.common.by import By
from helper import click_load_more,scroll_to_last,process_li
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    options=chrome_options
)
driver.get(LEADERBOARD_URL)
driver.maximize_window()
# to get all the data 
click_load_more(driver)
time.sleep(2)
data = []
scroll_to_last(driver,data)

time.sleep(3)

df = pd.DataFrame(data)
df = df.drop_duplicates(subset=["rank"]).sort_values(by='rank')
current_datetime = datetime.now()
# Format the date as a string (optional, depending on your needs)
current_date_string = current_datetime.strftime("%Y-%m-%d")
csv_file_path = f"./data/public_leaderboard_{current_date_string}.csv"
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")
driver.quit()



