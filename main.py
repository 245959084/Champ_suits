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
filter_line = df[df['preferred_role'] == lane]

champ_recommandation = ",".join(list(filter_line['champion']))
# display the result
st.write(f"Here are the recommandation for you: {champ_recommandation}.")