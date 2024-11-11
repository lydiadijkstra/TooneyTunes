README file for the Tooney Tunes project:

markdown
Code kopieren
# Tooney Tunes

Tooney Tunes is a group project that uses an SMS API to interact with users through a series of automated messages. The app provides users with a personalized experience based on their location and mood, delivering weather information, jokes, and music recommendations through SMS.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Tooney Tunes interacts with users by sending a sequence of SMS messages, where it:
1. Requests the user's location.
2. Fetches and sends the current weather for the provided location.
3. Asks the user to describe their current mood.
4. Sends a joke based on the user’s mood.
5. Recommends a song based on the mood.

This interactive SMS-based application aims to engage users in a fun and personalized way.

## Features
- **Location Request and Weather Information**: The user is asked to provide their location, after which the app retrieves and sends weather information for that location using a weather API.
- **Mood-based Interaction**: The user is asked about their mood, which the app uses to select and send an appropriate joke.
- **Music Recommendation**: Based on the user’s mood, the app recommends a song, enhancing the experience with a personalized music suggestion.
- **Automated Messaging Sequence**: Messages are sent with timed delays to provide a smooth flow of conversation.

## Technologies Used
- **Python**: Core language for developing the project.
- **SMS API**: Used for sending SMS messages to the user.
- **Weather API**: Fetches current weather information based on the user's location.
- **Spotify API**: Authenticates and retrieves song recommendations based on mood.
- **JSON Storage**: Stores and retrieves user information, like the last message, for continuity in interactions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tooney-tunes.git
Navigate to the project directory:
bash
Code kopieren
cd tooney-tunes
Install the required dependencies:
bash
Code kopieren
pip install -r requirements.txt
Set up your API keys:
SMS API Key: Sign up for an SMS sending service and add your key to the configuration.
Weather API Key: Sign up for a weather service API and add your key.
Spotify API Key: Register a Spotify application and add your client ID and secret.
Usage
Run the main.py script to start the application:
bash
Code kopieren
python main.py
The script will send a series of SMS messages to the specified phone number. Each message step includes:
Requesting the user’s location.
Fetching and sending weather information based on location.
Asking the user about their mood.
Sending a joke based on the user’s mood.
Recommending a song for the user’s mood.
Project Structure
The project structure is as follows:

plaintext
Code kopieren
TooneyTunes/
├── main.py                        # Main script to run the application
├── send_inBetween_message.py      # Sends a message between steps
├── send_retrieve_audio.py         # Handles mood-based song suggestion
├── send_retrieve_city.py          # Manages location requests and responses
├── get_weather_by_city.py         # Fetches weather information based on city
├── send_retrieve_mood.py          # Manages mood requests and responses
├── send_joke_by_mood.py           # Sends a joke based on mood
├── spotifyfunctions.py            # Handles Spotify authentication and song retrieval
├── storage_mood.py                # Manages storage and retrieval of the last message
├── requirements.txt               # List of required dependencies
└── last_message.json              # JSON file to store last message info
Key Modules
main.py: Controls the sequence of SMS interactions with the user.
send_inBetween_message.py: Sends interim messages between key steps.
send_retrieve_audio.py: Retrieves mood and provides song suggestions.
send_retrieve_city.py: Sends city request and retrieves user location.
get_weather_by_city.py: Fetches and formats weather info based on location.
send_retrieve_mood.py: Manages requests and retrieval of user mood.
send_joke_by_mood.py: Sends a joke based on the mood received.
spotifyfunctions.py: Authenticates with Spotify API and retrieves songs.
storage_mood.py: Stores the last message data for consistent interactions.
Contributing
To contribute to this project:

Fork the repository.
Create a new branch for your feature or bug fix:
bash
Code kopieren
git checkout -b feature-name
Commit your changes:
bash
Code kopieren
git commit -m "Add a new feature"
Push your branch:
bash
Code kopieren
git push origin feature-name
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

vbnet
Code kopieren

This README file provides an overview of the project, setup instructions, and details about each feature and module. Let me know if you need further modifications!
