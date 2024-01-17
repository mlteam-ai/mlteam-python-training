import requests
from dotenv import load_dotenv
import os
from speech_processing import SpeechProcessing

load_dotenv()
apininja_api_key = os.getenv("APININJA_API_KEY")
apininja_base_url = "https://api.api-ninjas.com/v1/jokes"

class JokesAgent:
    def __init__(self) -> None:
        self.speech_processor = SpeechProcessing()
    
    def handle_command(self, command):
        self.speech_processor.speak("I always have a good joke to tell ! Let me search inside of my machine brain...")
        joke = self.get_joke()
        if joke:
            self.speech_processor.speak(f"Here is a funny one: {joke}")
        else:
            self.speech_processor.speak("Sorry, I was not able to find a joke...")

    def get_joke(self, limit=1):
        try:
            params = {
                "limit": limit,
            }
            headers = {
                'X-Api-Key': apininja_api_key
            }
            response = requests.get(apininja_base_url, params=params, headers=headers)
            if response.status_code == 200:
                joke = response.json()[0]["joke"]
                return joke
        except Exception as error:
            print("An exception occured:", error)
        return None