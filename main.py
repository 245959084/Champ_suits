import streamlit as st
import numpy as np
import pandas as pd

# display some text
st.title("Number Doubler")
st.write("Enter a number and I'll double it for you.")
df = pd.read_csv("champ.csv")
df = df.dropna()

# ask for input
lane = st.selectbox(
    "Choose the lane you want to play",
    ["Top", "Jungle", "Mid", "ADC", "Support"]
)
filter_line = df[df['lane'] == lane]
#st.image("tes.img")

champ_recommandation = ",".join(list(filter_line['champion']))
first_champ = filter_line['champion'].iloc[0]
second_champ = filter_line['champion'].iloc[1]
third_champ = filter_line['champion'].iloc[2]

url1 = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{first_champ}_0.jpg"
url2 = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{second_champ}_0.jpg"
url3 = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{third_champ}_0.jpg"
# st.image(url1, caption=first_champ)
# st.image(url2, caption=second_champ)
# st.image(url3, caption=third_champ)
col1, col2, col3 = st.columns(3)

with col1:
    st.image(url1, caption=first_champ)

with col2:
    st.image(url2, caption=second_champ)

with col3:
    st.image(url3, caption=third_champ)
# display the result
st.write(f"Here are the recommandation for you: {champ_recommandation}.")