import requests
from send_retrieve_city import retrieve_city_after_user_reply


def get_weather_info(city_name):
    """
    retrieves the weather data from user location, outcome clear, clouds, haze, rain, mist, smoke, sunny
    """
    api_key = "2d5bf3dfe9001bb3e8e1ff79e43336d0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()
    weather_data_dict = {}

    # Check if the response contains the "cod" key with value 200 (success)
    if weather_data["cod"] == 200:
        # Extract relevant information
        main_data = weather_data["main"]
        temperature = round(main_data["temp"])
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_desc = weather_data["weather"][0]["main"]

        # Store the data in the dictionary
        weather_dict = {
            "temperature": f"{temperature}°C",
            "pressure": f"{pressure} hPa",
            "humidity": f"{humidity}%",
            "description": weather_desc
        }

        weather_data_dict[city_name] = weather_dict
        print(f"The weather is {weather_desc}")
        return weather_desc

    else:
        return "City not found or API request failed."


# def weather_type(weather_description):
#     if weather_description.lower() == "clear" or weather_description.lower() == "sunny":
#         return "sunny"
#     elif weather_description.lower() == "clouds" or weather_description.lower() == "rain" or\
#             weather_description.lower() == "smoke" or weather_description.lower() == "mist":
#         return "cloudy"
#     else:
#         return "other"


# def main():
#
#     phone_number = "4915566355818"
#     city_name = retrieve_city_after_user_reply(phone_number)
#
#     print(get_weather_info(city_name))
#
#
# if __name__ == "__main__":
#     main()
