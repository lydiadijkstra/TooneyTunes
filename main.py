import time
from send_inBetween_message import send_between_message_to_user
from send_retrieve_audio import get_mood, send_song_suggestion
from send_retrieve_city import send_request_city_to_user, retrieve_city_after_user_reply
from get_weather_by_city import get_weather_info
from send_retrieve_mood import send_request_mood_to_user, retrieve_mood_after_user_reply
from send_joke_by_mood import send_joke_to_user
from spotifyfunctions import authenticate_spotify, get_random_playlist_track
from storage_mood import get_last_message, save_last_message

# def main():
#     # Use phone number as a string
#     # phone_number = "015758872729"
#     phone_number = "4915566355818"
#
#     print(retrieve_mood_after_user_reply(phone_number))
#
#
# if __name__ == '__main__':
#     main()


def main():
    # Use phone number as a string
    phone_number = "4915566355818"

    # Send a joke to the user
    send_joke_to_user(phone_number)

    time.sleep(10)

    send_between_message_to_user(phone_number)

    time.sleep(7)

    mood = get_last_message(phone_number, file_path='last_message.json').strip().lower()
    send_song_suggestion(mood, phone_number)


if __name__ == '__main__':
    main()