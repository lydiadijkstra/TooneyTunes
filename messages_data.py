# import API_implementation

import requests
import json

### SMS API

url_sending_sms = "http://hackathons.masterschool.com:3030/sms/send"
url_get_messages = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"

# DATA SMS API
headers = {
        'Content-Type': 'application/json'
    }
body = {
  "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
  "baseUrl": "https://v36qlv.api.infobip.com",
  "phoneNumber": 491788580904,
  "message": "Hello, this is a test message from your terminal!"
  #"sender": "TooneyTunes" # commented out to be able to receive messages from user
}

# create a function to enter the current phone number:

body_requesting_emotion_reply = {
  "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
  "baseUrl": "https://v36qlv.api.infobip.com",
  "phoneNumber": 491788580904,
  "message": "Hello wonderful creature, please reply to this SMS with your current mood: relaxed? moody? hyped? -> and enjoy!"
  #"sender": "TooneyTunes" # commented out to be able to receive messages from user
}

"""
#used in def song_reply():
song_reply = {
  "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
  "baseUrl": "https://v36qlv.api.infobip.com",
  "phoneNumber": 491788580904,
  "message": "Thank you for sharing your mood - here is your Song for today: ",
  "sender": "TooneyTunes" # commented out to be able to receive messages from user
}
"""

# data requests:

# commented out to safe free sms sends as we only have limited free ones
# and I recommend to keep those for when we need to use them for testing:
    #send_sms = requests.post(url_sending_sms, headers=headers, data=json.dumps(body))
#send_sms = requests.post(url_sending_sms, headers=headers, data=json.dumps(body_requesting_emotion_reply))

get_messages_info = requests.get(url_get_messages)
#print(get_messages_info.text)
#print(type(get_messages_info))


# Testing to retrieve text messages from a specific phone number:
def get_user_reply_sms_list_sas():
    """
    Reads out the text messages from the SMS API - for 491788580904
    Converts <class 'requests.models.Response'> to json format.
    Creates List of user replies per sms.
    :return: text_replies_sms_user
    """
    get_messages_info_json = get_messages_info.json()
    # print(get_messages_info_json)
    # print(type(get_messages_info_json[0]))
    text_replies_sms_user_sas = []
    for message in get_messages_info_json:
        for phone_number, message_text in message.items():
            if phone_number == "491788580904":
                for single_sms_dict in message_text:
                    text_replies_sms_user_sas.append(single_sms_dict["text"])

    return text_replies_sms_user_sas

print(get_user_reply_sms_list_sas())

text_replies_sms_user_sas = get_user_reply_sms_list_sas()


def mood_jukebox():
    """
    Uses the List with returned user SMS to return information about mood.
    :return: current_mood
    """
    list_emotion_input = get_user_reply_sms_list_sas()

    # latest_emotion_user_input
    latest_user_input_mood = list_emotion_input[-1]
    # print(latest_user_input_mood)
    current_mood = ""
    if latest_user_input_mood == "relaxed":
        current_mood = "relaxed"
        print("Send relaxed song back")
    elif latest_user_input_mood == "moody":
        current_mood = "moody"
        print("Send happy song")
    elif latest_user_input_mood == "hyped":
        current_mood = "hyped"
        print("Send party song")
    else:
        current_mood = "Nichts funktioniert, error!"

    return current_mood


print(mood_jukebox())

def music_jukebox():
    """
    Calls mood_jukebox() -> to find the according Song
    :return: song_according_to_mood
    """
    mood_to_use = mood_jukebox()

    # return song_according_to_mood

def song_reply(song_according_to_mood):
    """
    uses music_jukebox() --> to send SMS back
    :return:
    """
    # song_according_to_mood - implement somehow in message
    song_reply = {
        "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
        "baseUrl": "https://v36qlv.api.infobip.com",
        "phoneNumber": 491788580904,
        "message": "Thank you for sharing your mood - here is your Song for today: {song_according_to_mood}",
        "sender": "TooneyTunes"
    }
    send_sms = requests.post(url_sending_sms, headers=headers, data=json.dumps(song_reply))


###########################
# in case we figure out a better way, this could be useful:

def get_all_user_replies_sms_list():
    """
    Reads ALL text messages from the SMS API and stores them in a List.
    Converts <class 'requests.models.Response'> to json format.
    :return: list_all_text_replies_sms_user
    """
    get_messages_info_json = get_messages_info.json()
    list_all_text_replies_sms_user = []
    for message in get_messages_info_json:
        for phone_number, message_text in message.items():
            for single_sms_dict in message_text:
                list_all_text_replies_sms_user.append(single_sms_dict["text"])

    return list_all_text_replies_sms_user

# print(get_all_user_replies_sms_list())
