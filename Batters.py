import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from MainApp import batterList


#Full table
data = pd.read_csv("batters.csv")
st.subheader(f"Batters")
st.write(data)

#Percentile Graph
st.subheader("Percentile Graph")

#Generate the percentile graph for wOBA
def generate_woba_percentile_graph(batterList):
    # Filter valid players
    valid_players = [
        player for player in batterList
        if player["wOBA"] != "N/A" and player["PA"] >= 5
    ]

    if not valid_players:
        return None  # No valid players

    # Sort by wOBA
    valid_players.sort(key=lambda x: x["wOBA"])

    # Extract data
    woba_values = [player["wOBA"] for player in valid_players]
    percentiles = np.linspace(0, 100, len(woba_values))

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(percentiles, woba_values, marker='o')
    ax.set_xlabel('Percentile')
    ax.set_ylabel('wOBA')
    ax.set_title('Percentile Graph of wOBA (PA ≥ 5)')

    return fig

#Display the percentile graph
#fig = generate_woba_percentile_graph(batterList)
#if fig:
  #st.pyplot(fig)
#else:
  #st.warning("No valid wOBA data available")
