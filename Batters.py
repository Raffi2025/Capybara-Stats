import streamlit as st
import pandas as pd

data = pd.read_csv("batters.csv")
st.subheader(f"Batters")
st.write(data)
