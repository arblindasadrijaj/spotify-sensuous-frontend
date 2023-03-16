import streamlit as st

import numpy as np
import pandas as pd
import requests

# Define the URL of your FastAPI application
fastapi_url = "https://api-sensuous-z4ulbtghrq-ew.a.run.app"

st.set_page_config(page_title="Song Explorer", page_icon=":musical_note:")

# App title
st.title("""Song Explorer :rocket:: _Discover Similar Songs Based on Your Favorites_
""")


# Add vinyl record image to header
st.image("raw_data/image.jpg")

st.markdown(""" Just pop your favorite song into our machine learning tool, and let us take care of the rest!
            We'll analyze the song's spectrogram and suggest other tracks that match your style, making it super easy to discover new music that you're bound to love! :hearts:
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
        try:
            playlist = predict_playlist(song, artist)
            st.write(f"We will be happy to make suggestions based on your choice: {song} by {artist}")
            st.markdown("### Our ML model suggests the following songs :raised_hands::")
            for index, item in enumerate(playlist):
                st.write(f"**{index + 1}.** {item[0]}\n by {item[1]}\n")
                st.write('---')
            st.write(":musical_note: Enjoy your playlist! :musical_note:", unsafe_allow_html=True)
        except:
            st.write(":rotating_light: Oops! Something went wrong. Please make sure you spelled the song and artist names correctly and try again.")

if __name__ == "__main__":
    main()
