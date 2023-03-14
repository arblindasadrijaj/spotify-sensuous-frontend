import streamlit as st

import numpy as np
import pandas as pd
import requests

# Define the URL of your FastAPI application
fastapi_url = "https://api-sensuous-z4ulbtghrq-ew.a.run.app"

st.title("""Song Explorer :rocket:: _Discover Similar Songs Based on Your Favorites_
""")

st.markdown(""" Our machine learning tool helps you **discover new songs** that you're likely to enjoy based on the characteristics of a song that you input.

Simply enter a song that you like, and our tool will analyze its spectrogram to identify its unique features. It will then suggest other songs with similar spectrograms, which you can explore and discover new music that you might not have found otherwise.

Give it a try and see how it can expand your musical horizons! :notes:
""")

def predict_playlist(song, artist):
    # Make a request to FastAPI
    response = requests.get(fastapi_url + "/predict", params={"song": song, "artist": artist})

    # Return the prediction result
    return response.json()['playlist']

def main():
    # Header 2
    st.markdown("### Enter a song here :musical_note:")

    # Input song
    song = str(st.text_input('You can write the title of your favorite song here, but make sure you spell it right :eyes:'))

    # Header 2
    st.markdown("### Enter an artist here :singer:")

    # Input artist
    artist = str(st.text_input('You can write the artist of your favorite song here, but make sure you spell it right :eyes:'))

    # Display appropriate message
    if song == '' or artist == '':
        pass  # don't display any message if input is empty
    else:
        playlist = predict_playlist(song, artist)
        st.write(f"We will be happy to make suggestions based on your choice: {song} by {artist}")
        st.markdown("### Our ML model suggests the following songs :raised_hands::")
        for index, item in enumerate(playlist):
            st.write(f"[{index + 1}]")
            st.write(f"Song: {item[0]}")
            st.write(f"Artist: {item[1]}")
            st.write('---')
        st.write(":musical_note: Enjoy your playlist! :musical_note:", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
