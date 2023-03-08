import streamlit as st

import numpy as np
import pandas as pd
import requests

st.markdown("""# Song Explorer :rocket:: _Discover Similar Songs Based on Your Favorites_
""")

st.markdown(""" Our machine learning tool helps you **discover new songs** that you're likely to enjoy based on the characteristics of a song that you input.

Simply enter a song that you like, and our tool will analyze its spectrogram to identify its unique features. It will then suggest other songs with similar spectrograms, which you can explore and discover new music that you might not have found otherwise.

Give it a try and see how it can expand your musical horizons! :notes:
""")



df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
