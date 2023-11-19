import pandas as pd
import streamlit as st
from constants import TITLE
from helper import load_data, get_daily_submits, get_latest
import seaborn as sns
import matplotlib.pyplot as plt


st.title(TITLE)
df = load_data()
multi = '''
### latest data :up:
'''
st.markdown(multi)
latest = get_latest(df)
st.dataframe(latest.drop(columns=["avatar_url"]), use_container_width=True)
submits_grouped_daily, participants_grouped_daily = get_daily_submits(df)


fig, ax = plt.subplots()
sns.barplot(submits_grouped_daily)
plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Submit Times')
plt.title('Daily Accumulated Submits')
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(12, 8))
sns.lineplot(participants_grouped_daily, marker='o', color="orange")
plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Teams')
st.pyplot(fig)
