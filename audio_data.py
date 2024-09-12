import spotifyfunctions as sf
import schedule
import time
import logging
import random
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy.exceptions import SpotifyException
import random
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

playlists = {
    "happy": "37i9dQZF1DXdPec7aLTmlC",
    "stressed": "37i9dQZF1E4sOTN8u2mWbq",
    "sleepy": "37i9dQZF1DWZd79rJ6a7lp"
}

# Authenticate Spotify
sp = sf.authenticate_spotify()

# Initialize global variables
happy_track = ""
happy_artist = ""
happy_link = ""

stressed_track = ""
stressed_artist = ""
stressed_link = ""

sleepy_track = ""
sleepy_artist = ""
sleepy_link = ""

music_dictionary = {}


def generate_music_dictionary():
    return {
        "happy": [
            {
                "title": happy_track,
                "artist": happy_artist,
                "link": happy_link
            }
        ],
        "stressed": [
            {
                "title": stressed_track,
                "artist": stressed_artist,
                "link": stressed_link
            }
        ],
        "sleepy": [
            {
                "title": sleepy_track,
                "artist": sleepy_artist,
                "link": sleepy_link
            }
        ]
    }


def update_track_info():
    global happy_track, happy_artist, happy_link
    global stressed_track, stressed_artist, stressed_link
    global sleepy_track, sleepy_artist, sleepy_link
    global music_dictionary

    try:
        new_artist_happy, new_track_happy, new_url_happy = sf.get_random_playlist_track(sp, playlists["happy"])
        new_artist_stressed, new_track_stessed, new_url_stressed = sf.get_random_playlist_track(sp,
                                                                                                playlists["stressed"])
        new_artist_sleepy, new_track_sleepy, new_url_sleepy = sf.get_random_playlist_track(sp, playlists["sleepy"])

        # Update global variables
        happy_artist = new_artist_happy
        happy_track = new_track_happy
        happy_link = new_url_happy

        stressed_artist = new_artist_stressed
        stressed_track = new_artist_stressed
        stressed_link = new_url_stressed

        sleepy_artist = new_artist_sleepy
        sleepy_track = new_track_sleepy
        sleepy_link = new_url_sleepy

        # Regenerate music_dictionary
        music_dictionary = generate_music_dictionary()

        logger.info(f"Updated track info for mood: {new_track_happy} by {new_artist_happy}")

    except Exception as e:
        logger.error(f"Error updating track: {e}")


def send_song_suggestion(mood, phone_number):
    global music_dictionary

    try:
        songtemporary = music_dictionary[mood]
        song_data = songtemporary[0]

        message = f"Your song suggestion for {mood}: {song_data['title']} by {song_data['artist']}. Spotify link: {song_data['link']}"

        body = {
            "phoneNumber": phone_number,
            "message": message
        }

        response = requests.post(url_send_sms_to_user, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            logger.info(f"Message sent to {phone_number}: {body['message']}")
            return current_time
        else:
            logger.warning(f"Failed to send SMS. Status code: {response.status_code}, Response: {response.text}")
            return None

    except Exception as e:
        logger.error(f"An error occurred in send_song_suggestion: {e}")
        return None


# Initialize music_dictionary
music_dictionary = generate_music_dictionary()

# Schedule the job to run every 10 seconds
schedule.every(10).seconds.do(update_track_info)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

        # Your main program logic here

except KeyboardInterrupt:
    print("Track updater stopped.")

def get_random_playlist_track(sp, playlist_id):

    #this you guys will understand easily with the json files provided
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