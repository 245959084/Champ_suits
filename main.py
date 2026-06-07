import streamlit as st
import numpy as np
import pandas as pd

# display some text
st.title("Champions Recommendation")
st.write("We will generate a champions list based on your preference.")
df = pd.read_csv("champ.csv")
df = df.dropna()

# Choosing line
lane = st.selectbox(
    "Choose the lane you want to play",
    ["Top", "Jungle", "Mid", "ADC", "Support"]
)
filter_lane = df[df['lane'] == lane]
if lane == "Top":
    st.image("img/lane/top.png", caption="Welcome to the top line!")
elif lane == "Jungle":
    st.image("img/lane/jungle.png", caption="Welcome to the jungle!")
elif lane == "Mid":
    st.image("img/lane/mid.png", caption="Welcome to the mid line!")
elif lane == "ADC":
    st.image("img/lane/bot.png", caption="Welcome to the bottom line, adc!")
elif lane == "Support":
    st.image("img/lane/bot.png", caption="Welcome to the bottom line, support!")
#st.write(filter_lane)

#choosing role
role  = st.selectbox(
    "Choose the role you are interested",
    ["Fighter", "Mage", "Assassin", "Marksman", "Support", "Tank"]
)
filter_role = filter_lane[filter_lane['role'] == role]
if filter_role.shape[0] == 0:
    st.error("No champion seems to fit your choice. Try different options or adjust previous selections.")
elif role == "Fighter":
    st.image("img/role/fighter.png", caption="You are capable of enduring and dealing certain damages.")
elif role == "Mage":
    st.image("img/role/mage.png", caption="Magic and abilities are your strongest weapons.")
elif role == "Assassin":
    st.image("img/role/assassin.png", caption="Instant burst damage, but avoid direct fight.")
elif role == "Marksman":
    st.image("img/role/marksman.png", caption="Range attack, teammates will look for your back.")
elif role == "Support":
    st.image("img/role/support.png", caption="Distract enemies and protect your allies.")
elif role == "Tank":
    st.image("img/role/tank.png", caption="Protect your teammates!")


#Choosing champion difficulty
difficulty  = st.selectbox(
    "Choose the difficulty to play your champion you will get",
    ["Easy", "Medium", "Hard"]
)
filter_diff = filter_role[filter_role['difficulty'] == difficulty]
if filter_diff.shape[0] == 0:
    st.error("No champion seems to fit your choice. Try different options or adjust previous selections.")
elif difficulty == "Easy":
    st.image("img/difficulty/easy.png", caption="Wise choice, these champions usually have stats.")
elif difficulty == "Medium":
    st.image("img/difficulty/medium.png", caption="I see you are ready to be on the next level.")
elif difficulty == "Hard":
    st.image("img/difficulty/hard.png", caption="Tough choice, these champions usually have high mobility and diffcult ability combination.")
#st.write(filter_diff)

#Choosing prefer attack range
range  = st.selectbox(
    "Choose the attack range you want",
    ["Short", "Medium", "Far"]
)
filter_range = filter_diff[filter_diff['attack_range'] == range]
if filter_range.shape[0] == 0:
    st.error("No champion seems to fit your choice. Try different options or adjust previous selections.")
else:
    champs = list(filter_range['champion'])
    champ_recommendation = ", ".join(champs)
    top_three = champs[:3]
    cols = st.columns(len(top_three))
    for col, champion in zip(cols, champs):
        url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champion}_0.jpg"
        with col:
            st.image(url, caption=champion)
    st.write(f"Here are the recommendation for you: {champ_recommendation}.")
#st.write(filter_range)
