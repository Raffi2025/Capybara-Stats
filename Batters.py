import streamlit as st
import pandas as pd

data = pd.read_csv("Batters.csv")
st.subheader(f"Batters ({len(data)} Entries):")
st.write(data)
