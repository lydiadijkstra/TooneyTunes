import random
import requests
import json
from datetime import datetime, timezone
from send_retrieve_mood import retrieve_mood_after_user_reply


# URL and headers for sending the SMS
url_send_sms_to_user = "http://hackathons.masterschool.com:3030/sms/send"
headers = {'Content-Type': 'application/json'}


def send_between_message_to_user(phone_number):

    # SMS body
    body = {
        "phoneNumber": phone_number,
        "message": "Have I made you smile? That is wonderful! Now it is time for our daily dose of music."
    }

    try:
        response = requests.post(url_send_sms_to_user, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            print()
            print(f"Message sent to {phone_number}: {body['message']}")

        else:
            print(f"Failed to send SMS. Status code: {response.status_code}, Response: {response.text}")

    except Exception as e:
        print(f"An error occurred in send_request_city_to_user: {e}")
