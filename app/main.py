import pandas as pd
import streamlit as st
from constants import TITLE, LEADERBOARD_URL
from helper import load_data, get_daily_submits, get_latest, get_daily_participants_by_rank
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kaggle Leadearbord Stats",
                   page_icon="📊", layout='wide')
st.title(TITLE)
link = f"[Leaderboard Link](f{LEADERBOARD_URL})"
print(link)
st.write(link)
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

multi = '''
### Check Each Team Progress :eye:
'''
st.markdown(multi)
team_names_with_rank = [f"{rank} {team_name}" for rank, team_name in zip(
    latest['rank'].astype(str), latest['team_name'])]

selected_teams = st.multiselect("Select team to display", team_names_with_rank)
if len(selected_teams) > 0:
    filtered_df = df[df['team_name'].isin(
        [a.split(' ', 1)[-1] for a in selected_teams])]
    fig, ax = plt.subplots(figsize=(12, 3))
    sns.lineplot(filtered_df, x='date', y='rank',
                 hue='team_name', marker="o")
    plt.title('Kaggle Rank Progression')
    plt.xticks(rotation=90)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(12, 3))
    sns.lineplot(filtered_df, x='date', y='score',
                 hue='team_name', marker="o")
    plt.title('Kaggle Score Progression')
    plt.xticks(rotation=90)
    st.pyplot(fig)
