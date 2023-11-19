# LeaderBoard Tracker

### Description

This repositry helps people track the publick leader board progress of Kaggle Competitions with the power of GitHub Actions. This repositry also includes data visualization application with Streamlit.


### How to track Other Leader Board 
- clone this repositry
- change the LEADERBOARD_URL to the one you like to track in the constants.py.
- check the action setting and change work flow permission "read and write permissions" 
- github actions will run the scraping script and udpate the repositry with newly scraped data
- Once the competition is over, you can disable the action.


### Scraping Demo
if you like to see how selenium scrape the data, you can comment out ```chrome_options.add_argument("--headless")``` in the scraper.py.
After running ```pip install -r requirements.txt```, your can run scraper.py


<p align='center' width="500">
<img src ='./scraping-demo.gif'/>
</p>

### Background

This project was created for [MLH 2023 Nov Hackathon](https://hackfest-november.devpost.com/)
