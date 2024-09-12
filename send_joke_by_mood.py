import random
import requests
import json
from datetime import datetime, timezone
from send_retrieve_mood import retrieve_mood_after_user_reply

# URL and headers for sending the SMS
url_send_sms_to_user = "http://hackathons.masterschool.com:3030/sms/send"
headers = {'Content-Type': 'application/json'}

# Reply data based on mood
reply_data = {
    "happy": ["You are right Baby! Life is short. Smile while you still have teeth.",
              "You are right Baby! Do not take life too seriously. You will never get out of it alive.",
              "You are right Baby! While happiness might not make you younger, it sure makes you more immature!"],
    "stressed": ["Relax! Don’t worry about the world coming to an end today. It is already tomorrow in Australia.",
                 'Relax! "Stressed" spelled backwards is desserts. Just turn around and get yourself a sweet treat!',
                 "Relax! You’re not a Wi-Fi signal — there is no need to constantly be under pressure!"],
    "sleepy": ["Sleepy? Just imagine your partner has found out what you were really doing last night — that will wake you up faster than coffee!",
               "sleepy? Just quit your job and go to bed man! Even your phone needs to recharge, and it does not have to deal with life!",
               "Sleepy? How dare you! The zombies are catching up!"]
}


# Function to retrieve a random joke based on the user's mood
def get_random_joke(current_mood):

    cleaned_mood = current_mood.strip().lower()

    if cleaned_mood in reply_data:
        random_reply = random.choice(reply_data[cleaned_mood])
        return random_reply
    else:
        # Provide a default message if the mood is not recognized
        default_message = "Oops! Looks like I'm not ready with a response for that mood today!"
        print(default_message)
        return default_message

# Function to simulate retrieving the user's mood based on their reply


# Function to send a joke to the user
def send_joke_to_user(phone_number):
    try:
        # Get the current time when sending the SMS
        current_time = datetime.now(timezone.utc).isoformat()

        # Retrieve the user's mood from the last reply
        last_message = retrieve_mood_after_user_reply(phone_number)
        current_mood = last_message.lower()  # Convert the mood to lowercase
        print(f"User's mood is: {current_mood}")

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