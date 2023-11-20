import pandas as pd
import streamlit as st
from constants import TITLE
from helper import load_data, get_daily_submits, get_latest, get_daily_participants_by_rank
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.title(TITLE)
df = load_data()
multi = '''
### latest data :up:
'''
st.markdown(multi)
latest = get_latest(df)
st.data_editor(
    latest,
    column_config={
        "avatar_url": st.column_config.ImageColumn(
            "Avatar Image", help="Higheset rank User Avatar"
        )
    },
    use_container_width=True,
    hide_index=True,

)

multi = '''
### Competition Stats :+1:
'''
st.markdown(multi)
col1, col2 = st.columns(2)

submits_grouped_daily = get_daily_submits(df)

fig, ax = plt.subplots()
sns.barplot(submits_grouped_daily)
plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Submit Times')
plt.title('Total Submissions in the Competition')
with col1:
    st.pyplot(fig)


fig, ax = plt.subplots()
sns.lineplot(data=get_daily_participants_by_rank(
    df), markers=True, dashes=False)
plt.title('Daily Growth of Participants by Kaggle Rank')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Number of Participants')
plt.legend(title='Kaggle Rank', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
with col2:
    st.pyplot(fig)
