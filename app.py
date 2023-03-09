import streamlit as st

import numpy as np
import pandas as pd
import requests

st.title("""Song Explorer :rocket:: _Discover Similar Songs Based on Your Favorites_
""")

st.markdown(""" Our machine learning tool helps you **discover new songs** that you're likely to enjoy based on the characteristics of a song that you input.

Simply enter a song that you like, and our tool will analyze its spectrogram to identify its unique features. It will then suggest other songs with similar spectrograms, which you can explore and discover new music that you might not have found otherwise.

Give it a try and see how it can expand your musical horizons! :notes:
""")

def main():
    # Header 2
    st.markdown("## Enter a song here")

    # Input
    song = str(st.text_input('You can write the title of your favorite song here, but make sure you spell it right :eyes:'))

    # Define the accepted songlist
    songlist = ["we will rock you", "another one bites the dust", "the show must go on"]

    # Only allow songs from the accepted songlist
    valid_input = True
    if song != '' and song not in songlist:
        valid_input = False

    # Display appropriate message
    if song == '':
        pass  # don't display any message if input is empty
    elif valid_input:
        st.write('We will be happy to make suggestions based on your choice:', song)
    else:
        st.write('Sorry, that song is not in our list. Please choose from:', songlist)

if __name__ == "__main__":
    main()
