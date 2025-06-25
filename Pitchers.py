import streamlit as st
import pandas as pd

data = pd.read_csv("pitchers.csv")
st.subheader(f"Pitchers ({len(data)} Entries):")
st.write(data)
