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

def no_more_loading(driver,times=0):
    times +=1
    li_elements = driver.find_elements(By.TAG_NAME,'li')
    li_num = len(li_elements)
    elem = driver.find_element(By.TAG_NAME, "html")
    elem.send_keys(Keys.END)
    time.sleep(2)
    li_elements = driver.find_elements(By.TAG_NAME,'li')
    after_li_num = len(li_elements)
    print (after_li_num, li_num)
    return after_li_num > li_num or times==1
    
# Assuming 'driver' is your WebDriver instance
# Make sure to replace this with your actual WebDriver instance

import time

# Repeat scroll-down action until scrollbar is at the bottom
def scroll_to_last(driver):
    while no_more_loading(driver):
        # You can add additional actions or processing here if needed
        print("Scrolling down...")
        time.sleep(2)