import time
import requests
import json
from datetime import datetime, timezone
import audio_data
import spotifyfunctions
import send_retrieve_mood


# URLs
url_send_sms_to_user = "http://hackathons.masterschool.com:3030/sms/send"
url_retrieve_sms_from_user = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"

# Headers
headers = {'Content-Type': 'application/json'}

playlists = {
    "happy": "37i9dQZF1DXdPec7aLTmlC",
    "stressed": "37i9dQZF1E4sOTN8u2mWbq",
    "sleepy": "37i9dQZF1DWZd79rJ6a7lp"
}


def get_mood(phone_number):
    return send_retrieve_mood.retrieve_mood_after_user_reply(phone_number)


def send_song_suggestion(mood, phone_number):
    # songtemporary = audio_data.music_dictionary[mood]
    # localmood = mood
    # song_data = songtemporary[0]
    # example
    sp = spotifyfunctions.authenticate_spotify()
    playlist_id = playlists[mood]  # Replace with your playlist ID
    artist, track, url = audio_data.get_random_playlist_track(sp, playlist_id)

    message = f"Your song suggestion for {mood}: {track} by {artist}. Spotify link: {url}"
    #message = f"your song suggestion for today {songtemporary["artist"]} - {songtemporary["title"]} Spotifylink: {songtemporary["link"]}"

    #message = f"Have I made you smile? That is wonderful! Now it is time for our daily dose of music."

    body = {
        "phoneNumber": phone_number,
        "message": message
    }
    
    try:
        response = requests.post(url_send_sms_to_user, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            print(f"Message sent to {phone_number}: {body['message']}")

        else:
            print(f"Failed to send SMS. Status code: {response.status_code}, Response: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred in send_request_mood_to_user: {e}")
        return None

# def main():
#     # Use phone number as a string
#     phone_number = "4915566355818"
#
#     # Start the process of sending SMS and retrieving the reply
#     Mood_test = "happy"
#     send_song_suggestion(Mood_test, phone_number)
#
#
# if __name__ == '__main__':
#     main()