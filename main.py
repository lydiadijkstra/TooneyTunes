import messages_data


def main():
    #messages_data.sending_message()
    text_replies_sms_user_sas = messages_data.send_and_get_user_reply_sms_list_sas()
    current_mood = messages_data.mood_jukebox(text_replies_sms_user_sas)
    song_options_according_to_mood = messages_data.music_jukebox(current_mood)
    messages_data.song_reply(song_options_according_to_mood)  # sends: send_sms_song_reply


if __name__ == "__main__":
    main()
