import pandas as pd
import streamlit as st
from constants import TITLE
from helper import load_data, get_daily_submits
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


st.title(TITLE)
df = load_data()
st.dataframe(df, use_container_width=True)
submits_grouped_daily, participants_grouped_daily = get_daily_submits(df)

st.dataframe(submits_grouped_daily)

fig, ax = plt.subplots()
sns.barplot(submits_grouped_daily)
plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Submit Times')
plt.title('Daily Accumulated Submit')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.lineplot(participants_grouped_daily)
plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Teams')
plt.title('Number of Teams')
st.pyplot(fig)
