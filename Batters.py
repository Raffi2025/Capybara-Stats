import streamlit as st
import pandas as pd


#Full table
data = pd.read_csv("batters.csv")
st.subheader(f"Batters")
st.write(data)

#Percentile Graph
st.subheader("Percentile Graph")

