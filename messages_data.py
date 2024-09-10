import audio_data
import requests
import json
import random

#### SMS API
## DATA SMS API

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

body_requesting_emotion_reply = {
    "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
    "baseUrl": "https://v36qlv.api.infobip.com",
    "phoneNumber": 491788580904,
    "message": "Hello wonderful creature, please reply to this SMS with your current mood: happy? stressed? sleepy?"
    #"sender": "TooneyTunes" # commented out to be able to receive messages from user
}
#used in def song_reply():
song_reply = {
    "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
    "baseUrl": "https://v36qlv.api.infobip.com",
    "phoneNumber": 491788580904,
    "message": "Thank you for sharing your mood - here is your Song for today: {song_according_to_mood}",
    "sender": "TooneyTunes"
}


## data requests:
#send_sms = requests.post(url_sending_sms, headers=headers, data=json.dumps(body))

def sending_message():
    url_sending_sms = "http://hackathons.masterschool.com:3030/sms/send"
    url_get_messages = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"
    send_sms_asking_for_mood = requests.post(url_sending_sms, headers=headers,
                                             data=json.dumps(body_requesting_emotion_reply))
    get_messages_info = requests.get(url_get_messages)


# Retrieve text messages from a specific phone number:
def send_and_get_user_reply_sms_list_sas():
    """
    Reads out the text messages from the SMS API - for 491788580904
    Converts <class 'requests.models.Response'> to json format.
    Creates List of user replies per sms.
    :return: text_replies_sms_user
    """
    url_sending_sms = "http://hackathons.masterschool.com:3030/sms/send"
    url_get_messages = "http://hackathons.masterschool.com:3030/team/getMessages/TooneyTunes"
    send_sms_asking_for_mood = requests.post(url_sending_sms, headers=headers,
                                             data=json.dumps(body_requesting_emotion_reply))
    get_messages_info = requests.get(url_get_messages)
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


def mood_jukebox(list_emotion_input):
    """
    Uses the List with returned user SMS to return information about mood.
    :return: current_mood
    """
    list_emotion_input = send_and_get_user_reply_sms_list_sas()
    latest_user_input_mood = list_emotion_input[-1]
    # print(latest_user_input_mood)
    current_mood = ""
    if latest_user_input_mood == "happy":
        current_mood = "happy"
    elif latest_user_input_mood == "stressed":
        current_mood = "stressed"
    elif latest_user_input_mood == "sleepy":
        current_mood = "sleepy"
    else:
        current_mood = "Error!"

    return current_mood


#print(mood_jukebox())


def music_jukebox(current_mood):
    """
    Calls mood_jukebox() -> to find the according Song
    :return: song_options_according_to_mood
    """
    # mood_to_use = "sleepy" - testing leftover

    mood_to_use = current_mood
    song_options_according_to_mood = []
    for mood, song_collection in audio_data.music_dictionary.items():
        if mood_to_use == mood:
            for song_details in song_collection:
                song_options_according_to_mood.append((song_details["artist"], song_details["title"]))

    return song_options_according_to_mood


def song_reply(song_options_according_to_mood):
    """
    uses music_jukebox() --> to send SMS back
    :return:
    """
    # randomize over tuples:
    song_tuple_choice = song_options_according_to_mood.pop(random.randrange(len(song_options_according_to_mood)))
    # adding the scraped song:

    song_reply = {
        "apiToken": "ff5545473ee5ccf545e77dd52ed2a62e-6e416a63-6fa1-414a-80b6-d784479d61c8",
        "baseUrl": "https://v36qlv.api.infobip.com",
        "phoneNumber": 491788580904,
        "message": "Thank you for sharing your mood - here is your Song for today: {song_according_to_mood}",
        "sender": "TooneyTunes"
    }
    song_tuple_choice = song_options_according_to_mood.pop(random.randrange(len(song_options_according_to_mood)))
    #one could still unpack the tuple and present it in a nicer way in the message
    song_reply[
        "message"] = "Thank you for sharing your mood - here is your Song for today: " + f"{song_tuple_choice} " + "!!!"

    # sending the final message
    url_sending_sms = "http://hackathons.masterschool.com:3030/sms/send"
    send_sms_song_reply = requests.post(url_sending_sms, headers=headers, data=json.dumps(song_reply))


##################################################################
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


#print(get_all_user_replies_sms_list())

# second version for extracting a random song:
def get_random_song(current_mood):
    music_data = audio_data.music_dictionary
    if current_mood in music_data:
        random_song = random.choice(audio_data.music_dictionary[current_mood])
        print(f"Title: {random_song['title']}, Artist: {random_song['artist']}")
    else:
        print("Mood not found")


# get_random_song("sleepy")
