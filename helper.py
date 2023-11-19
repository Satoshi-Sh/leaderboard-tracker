# Function to check if the "Load More" button exists and click it
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from constants import REPETITIONS
from bs4 import BeautifulSoup


def click_load_more(driver):
    try:
        load_more_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@data-testid="load-more-section"]/div/button')))
        driver.execute_script(
            "arguments[0].scrollIntoView();", load_more_button)
        load_more_button.click()
        print('clicked')
        return
    except Exception as e:
        print(str(e))

# Repeat scroll-down action until scrollbar is at the bottom


def scroll_to_last(driver, data):
    elem = driver.find_element(By.TAG_NAME, "html")
    for _ in range(REPETITIONS):
        extract_data(driver, data)
        elem.send_keys(Keys.END)
        time.sleep(0.1)


def get_data_from_image(span):
    # TODO get highest rank person
    first_url_style = span.select_one(
        'div[data-testid="avatar-image"]')['style']
    first_url_start = first_url_style.find('url("') + len('url("')
    first_url_end = first_url_style.find('")', first_url_start)
    first_url = first_url_style[first_url_start:first_url_end]

    # Extract the stroke color from the style attribute of the first path
    path_element = span.select_one('path')
    # grandmaster doesn't have path
    if not path_element:
        kaggle_rank = 'grand master'
    else:
        first_stroke_color_style = path_element['style']
        first_stroke_color_start = first_stroke_color_style.find(
            'stroke: rgb(') + len('stroke: rgb(')
        first_stroke_color_end = first_stroke_color_style.find(
            ');', first_stroke_color_start)
        first_stroke_color = first_stroke_color_style[first_stroke_color_start:first_stroke_color_end]

        dic = {
            '28, 205, 118': "novice",
            '32, 190, 255': "contributor",
            '101, 31, 255': "expert",
            '255, 92, 25': "master",
        }

        kaggle_rank = dic.get(first_stroke_color, "other")

    return [first_url, kaggle_rank]

# process data from html
# rank| empty| teamname| image|score| submit_times| last submit| empty|


def process_li(li):
    try:
        spans = li.find_all('span')
        rank = int(spans[0].text)
        team_name = spans[2].text

        all_images = spans[3].find_all('a')
        highest_kaggle_rank = 'novice'
        if len(all_images) > 1:
            for image in all_images:
                [url, kaggle_rank] = get_data_from_image(image)
                if kaggle_rank == "grand master":
                    imageUrl = url
                    highest_kaggle_rank = kaggle_rank
                elif kaggle_rank == "master" and highest_kaggle_rank not in ["grand master"]:
                    imageUrl = url
                    highest_kaggle_rank = kaggle_rank
                elif kaggle_rank == "expert" and highest_kaggle_rank not in ["grand master", "master"]:
                    imageUrl = url
                    highest_kaggle_rank = kaggle_rank
                elif kaggle_rank == "contributor" and highest_kaggle_rank not in ["grand master", "master", "expert"]:
                    imageUrl = url
                    highest_kaggle_rank = kaggle_rank
                elif kaggle_rank == "other":
                    imageUrl = url
                    highest_kaggle_rank = kaggle_rank

        else:
            [imageUrl, highest_kaggle_rank] = get_data_from_image(
                spans[3])
        score = float(spans[4].text)
        submit_times = spans[5].text
        last_submit = spans[6].text
        print({'rank': rank, 'team_name': team_name, 'avatar_url': imageUrl, 'highest_kaggle_rank': highest_kaggle_rank,
               'score': score, 'submit_times': submit_times, 'last_submit': last_submit})
        return {'rank': rank, 'team_name': team_name, 'avatar_url': imageUrl, 'highest_kaggle_rank': highest_kaggle_rank, 'score': score, 'submit_times': submit_times, 'last_submit': last_submit}
    except Exception as e:
        print(str(e))
        return None

# need to extract data for each scroll since old data get deleted


def extract_data(driver, data):
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    ul_elements = soup.find_all("ul", class_="km-list")
    lis = ul_elements[2].find_all("li")
    for li in lis:
        processed = process_li(li)
        if processed:
            data.append(processed)
