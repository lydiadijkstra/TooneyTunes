import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
import random
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

##this is for the env file which is importand for the way the spotify api gives you access
##we need this for spotify "pip install python-dotenv"
##this os base64 stuff is for the api security and just copy paste from the yt video and spotipy
## request with import post,get i dont know if i used it but the guy from the net

load_dotenv()


def authenticate_spotify():
    ###Client Credentials Flow on spotipy https://spotipy.readthedocs.io/en/2.24.0/#client-credentials-flow heres the link
    """this thing actually generates a token each time the function is called based on the env file here"""
    """other wise we could use no token for accessing the api but our limit would be restricted to 10 minutes usage
    this is all copy pasted """
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET')
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp


def get_random_playlist_track(sp, playlist_id):
    # this you guys will understand easily with the json files provided
    # its just a random value to the results"items" key
    try:
        # Fetch tracks from the playlist
        results = sp.playlist_tracks(playlist_id)

        # Select a random track
        random_track = random.choice(results['items'])

        # values for artist name, spotify url (2 options) and track name
        artist_name = random_track['track']['artists'][0]['name']
        spotifyurl2 = random_track['track']['artists'][0]['external_urls']['spotify']
        track_name = random_track['track']['name']
        spotify_url = f"https://open.spotify.com/track/{random_track['track']['id']}"

        return artist_name, track_name, spotifyurl2

    except SpotifyException as e:
        print(f"An error occurred: {e}")
        return None, None, None


playlists = {"happy": "37i9dQZF1DXdPec7aLTmlC",
             "stressed": "7vgzPGibRcse3QY4d9316n",
             "sleepy": "37i9dQZF1DWZd79rJ6a7lp"}