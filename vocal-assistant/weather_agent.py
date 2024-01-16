
from dotenv import load_dotenv
import requests
import os
from speech_processing import SpeechProcessing
from openai_agent import OpenAIAgent

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
weather_base_url = "http://api.weatherapi.com/v1/current.json"

class WeatherAgent:
    def __init__(self) -> None:
        self.openai_agent = OpenAIAgent()
        self.speech_processor = SpeechProcessing()

    def getWeather(self, location):
        params = {
            "key": weather_api_key,
            "q": location,
            "aqi":"no"
        }
        response = requests.get(weather_base_url, params)
        if response.status_code != 200:
            return None
        else:
            data = response.json()
            weather_data = {
                "location": data["location"]["name"],
                "condition": data["current"]["condition"]["text"],
                "temprature": data["current"]["temp_c"]
            }
            return weather_data
    
    def handle_command(self, command):
        location = self.openai_agent.extract_information('location', command)
        if location == None or location == 'none':
            command = ""
            while command == "":
                self.speech_processor.speak("Please specify a location for me to give you the current weather.")
                command = self.speech_processor.listen()
            self.handle_command(command)
        else:
            weather_data = self.getWeather(location)
            self.process_weather_data(weather_data)

    def process_weather_data(self, data):
        if data:
            weather_msg = f"Currently in {data['location']}, the weather condition is : {data['condition']}, and the temprature is : {data['temprature']} degrees."
            self.speech_processor.speak(weather_msg)
        else:
            self.speech_processor.speak("Could not get the weather data from weatherapi.com. Please try again later.")

