# LeaderBoard Tracker

### Description

This repository helps people track the public leaderboard progress of Kaggle Competitions with the power of GitHub Actions. This repository also includes a data visualization application with Streamlit.


### How to track Other Leader Board 
- Fork this repository
- change the LEADERBOARD_URL to the one you like to track in the constants.py.
- check the action setting and change workflow permission "read and write permissions" 
- GitHub actions will run the scraping script and update the repository with newly scraped data
- Once the competition is over, you can disable the action.


### Scraping Demo
if you like to see how selenium scrapes the data, you can comment out ```chrome_options.add_argument("--headless")``` in the scraper.py.
After running ```pip install -r requirements.txt```, your can run scraper.py


<p align='center' width="500">
<img src ='./scraping-demo.gif'/>
</p>

### Background

This project was created for [MLH 2023 Nov Hackathon](https://hackfest-november.devpost.com/)
