# Function to check if the "Load More" button exists and click it
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def click_load_more(driver):
    try:
        load_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//div[@data-testid="load-more-section"]/div/button')))
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        load_more_button.click()
        print('clicked')
        return;
    except Exception as e:
        print(str(e))

# Repeat scroll-down action until scrollbar is at the bottom
def scroll_to_last(driver):
    times= 0
    while True:
        times+=1
        li_elements = driver.find_elements(By.TAG_NAME,'li')
        li_num = len(li_elements)
        elem = driver.find_element(By.TAG_NAME, "html")
        # 
        for _ in range(10):
           elem.send_keys(Keys.END)
           time.sleep(1)
        li_elements = driver.find_elements(By.TAG_NAME,'li')
        after_li_num = len(li_elements)
        print (after_li_num, li_num)
        if after_li_num == li_num  and times > 1:
            break
        