import streamlit as st
import pandas as pd

data = pd.read_csv("batters.csv")
st.subheader(f"Batters ({len(data)} Entries):")
st.write(data)
