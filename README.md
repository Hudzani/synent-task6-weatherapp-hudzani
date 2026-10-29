Task 6: Weather App(API Integration)

    A command line app that fatches real time weather for any city using the OpenWeather API.

**Features**

    -Input a city name
     -Display temperature, humidity and weather condition 
     -Handles invalid cities, network errors and invalid API keys
     -API key is loaded from a '.env' file and never hard coded

**Setup**

    1.Install the liabraries: 
    -pip install requests python-dotenv
    2.Get a free API key from openweathermap.org.

    3.Copy 'Weather_App/.env.example to 'Weather_App/.env' and add your key:

        OPENWEATHER_API_KEY=your_key_here

**How to run**

    python weather.py

**Example output

    Weather App

    Enter city name(or 'q' to quit): Johannesburg

    weather in Johannesburg, ZA
    Temperature: 21.02 °C
    Humidity:    59%
    Condition:   Few Clouds
    
**Security note**

    The API key is loaded from a '.env' file, which is listed in '.gitignore' so it is never uploaded to Github.

**Author**
Hudzani