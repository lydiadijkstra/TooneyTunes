import random
import requests
import json
from datetime import datetime, timezone
from send_retrieve_mood import retrieve_mood_after_user_reply


music_data = {
    "happy": [
        {
            "title": "Happy",
            "artist": "Pharrell Williams",
            "link": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        },
        {
            "title": "Can't Stop the Feeling!",
            "artist": "Justin Timberlake",
            "link": "https://www.youtube.com/watch?v=ru0K8uYEZWw"
        },
        {
            "title": "Walking on Sunshine",
            "artist": "Katrina and the Waves",
            "link": "https://www.youtube.com/watch?v=iPUmE-tne5U"
        },
    ],

    "stressed": [
        {
            "title": "The Lazy Song",
            "artist": "Bruno Mars",
            "link": "https://www.youtube.com/watch?v=kTsfbgk7VjQ"
        },
        {
            "title": "I'm Gonna Be (500 Miles)",
            "artist": "Proclaimers",
            "link": "https://www.youtube.com/watch?v=tbNlMtqrYS0"
        },
        {
            "title": "Eat It",
            "artist": "Weird Al Yankovic",
            "link": "https://www.youtube.com/watch?v=ZcJjMnHoIBI"
        }
    ],

    "sleepy": [
        {
            "title": "Eye of the Tiger",
            "artist": "Survivor",
            "link": "https://www.youtube.com/watch?v=btPJPFnesV4"
        },
        {
            "title": "Uptown Funk",
            "artist": "Survivor",
            "link": "https://www.youtube.com/watch?v=OPf0YbXqDm0"
        },
        {
            "title": "Wake Me Up",
            "artist": "Avicii",
            "link": "https://www.youtube.com/watch?v=5y_KJAg8bHI"
        }
    ]
}

# Retrieve the user's mood from the last reply
last_message = retrieve_mood_after_user_reply(phone_number)
current_mood = last_message.lower()  # Convert the mood to lowercase


def get_random_song(current_mood):

    cleaned_mood = current_mood.strip().lower()

    if cleaned_mood in music_data:

        random_song = random.choice(music_data[current_mood])

        print(f"🎵 Title: {random_song['title']}, Artist: {random_song['artist']}\n"
              f"👉 Click the link: {random_song['link']}")
        return random_song

    else:
        print(f"Uh-oh, I don't have a song ready for {current_mood}. Try again later?")


def send_hard_code_song_to_user(phone_number):
    try:
        # Get the current time when sending the SMS
        current_time = datetime.now(timezone.utc).isoformat()



        # Get a random joke based on the mood
        message = get_random_joke(current_mood)
        print(f"Joke to send: {message}")

        # SMS body
        body = {
            "phoneNumber": phone_number,
            "message": message
        }

        # Send the message via POST request
        response = requests.post(url_send_sms_to_user, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            print(f"Message sent to {phone_number}: {body['message']}")
            print(f"Message sent at: {current_time}")
        else:
            print(f"Failed to send SMS. Status code: {response.status_code}, Response: {response.text}")

    except Exception as e:
        print(f"An error occurred in send_joke_to_user: {e}")


# def main():
#     # Use phone number as a string
#     phone_number = "4915566355818"
#
#     # Send a joke to the user
#     send_joke_to_user(phone_number)
#
#
# if __name__ == '__main__':
#     main()