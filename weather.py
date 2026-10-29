import os
import requests
from dotenv import load_dotenv

# Load the API from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch and display current weather for a city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(URL, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection and try again.")
        return

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity:    {data['main']['humidity']}%")
        print(f"Condition:   {data['weather'][0]['description'].title()}")
    elif response.status_code == 404:
        print("City not found. Check the spelling and try again.")
    elif response.status_code == 401:
        print("Invalid API key. Check your .env file")
    else:
        print(f"Something went wrong (error {response.status_code}).")


def main():
    print("Weather App")
    if not API_KEY:
        print("API key missing. Add OPENWEATHER_API_KEY to your .env file.")
        return

    while True:
        city = input("\nEnter city name (or 'q' to quit): ").strip()
        if city.lower() == "q":
            break
        if not city:
            print("Please enter a city name.")
            continue
        get_weather(city)


main()