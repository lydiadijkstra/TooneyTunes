import time
import requests
import json
from datetime import datetime, timezone
from send_retrieve_city import retrieve_last_reply_from_user, retrieve_city_after_user_reply
from get_weather_by_city import get_weather_info
from storage_mood import save_last_message

# URLs
url_send_sms_to_user = "http://hackathons.masterschool.com:3030/sms/send"
url_retrieve_sms_from_user = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"

# Headers
headers = {'Content-Type': 'application/json'}


def send_request_mood_to_user(phone_number):
    # Get the current time when sending the SMS
    current_time = datetime.now(timezone.utc).isoformat()

    city_name = retrieve_city_after_user_reply(phone_number)

    current_weather = get_weather_info(city_name)

    message = f"In {city_name}, the weather is {current_weather} right now. How are you feeling today? happy, stressed, or sleepy?"

    # SMS body
    body = {
        "phoneNumber": phone_number,
        "message": message
    }

    try:
        response = requests.post(url_send_sms_to_user, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            print(f"Message sent to {phone_number}: {body['message']}")
            print(f"Message sent at: {current_time}")
            return current_time
        else:
            print(f"Failed to send SMS. Status code: {response.status_code}, Response: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred in send_request_mood_to_user: {e}")
        return None


def retrieve_mood_after_user_reply(phone_number):
    # Send the SMS and get the time it was sent
    last_sent_time = send_request_mood_to_user(phone_number)

    if last_sent_time is None:
        print("Could not send message, aborting polling.")
        return None

    # Pause before polling
    time.sleep(15)

    # Polling for a reply
    while True:
        time.sleep(15)  # Wait before checking again
        last_message, received_at = retrieve_last_reply_from_user(phone_number)

        if last_message and received_at > last_sent_time:
            print()
            print(f"User replied: {last_message}, received at {received_at}")

            save_last_message(phone_number, last_message, file_path='last_message.json')

            return last_message


