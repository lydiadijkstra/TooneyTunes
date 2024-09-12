import json
import os


def save_last_message(phone_number, last_message, file_path='last_message.json'):
    # Check if file exists, if not, create an empty dictionary
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # Save phone number and last message to the file
    data[phone_number] = last_message

    with open(file_path, 'w') as f:
        json.dump(data, f)


def get_last_message(phone_number, file_path='last_message.json'):
    # Check if file exists, if not, return None
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data.get(phone_number)
    return None


# def retrieve_and_save_message(phone_number, retrieve_message_func):
#     # Try to get the last message from the file first
#     last_message = get_last_message(phone_number)
#     if last_message:
#         print("Message retrieved from file.")
#         return last_message
#
#     # If no message is found in the file, call the API function
#     last_message = retrieve_message_func(phone_number)
#
#     # Save the new message to the file
#     save_last_message(phone_number, last_message)
#     print("Message retrieved from API and saved to file.")
#
#     return last_message