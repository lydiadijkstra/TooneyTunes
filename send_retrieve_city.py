import time
import requests
import json
from datetime import datetime, timezone

# URLs
url_send_sms_to_user = "http://hackathons.masterschool.com:3030/sms/send"
url_retrieve_sms_from_user = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"

# Headers
headers = {'Content-Type': 'application/json'}


def send_request_city_to_user(phone_number):
    # Get the current time when sending the SMS
    current_time = datetime.now(timezone.utc).isoformat()

    # SMS body
    body = {
        "phoneNumber": phone_number,
        "message": "Welcome to TooneyTunes! Where do you live please?"
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
        print(f"An error occurred in send_request_city_to_user: {e}")
        return None


def retrieve_last_reply_from_user(phone_number):
    try:
        response = requests.get(url_retrieve_sms_from_user, headers=headers)
        if response.status_code == 200:
            messages = response.json()

            for user in messages:
                if phone_number in user:
                    user_messages = user[phone_number]
                    last_message = user_messages[-1]  # Get the latest message
                    return last_message['text'], last_message['receivedAt']
        else:
            print(f"Failed to retrieve messages. Status code: {response.status_code}, Response: {response.text}")
            return None, None
    except Exception as e:
        print(f"An error occurred in retrieve_last_reply_from_user: {e}")
        return None, None


def retrieve_city_after_user_reply(phone_number):
    # Send the SMS and get the time it was sent
    last_sent_time = send_request_city_to_user(phone_number)

    if last_sent_time is None:
        print("Could not send message, aborting polling.")
        return None

    # Pause before polling
    time.sleep(15)

    # Polling for a reply
    while True:
        time.sleep(10)  # Wait before checking again
        last_message, received_at = retrieve_last_reply_from_user(phone_number)

        if last_message and received_at > last_sent_time:
            print()
            print(f"User replied: {last_message}, received at {received_at}")
            return last_message


# def main():
#     # Use phone number as a string
#     phone_number = "4915566355818"
#
#     # Start the process of sending SMS and retrieving the reply
#     print(retrieve_city_after_user_reply(phone_number))
#
#
# if __name__ == '__main__':
#     main()