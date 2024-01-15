import openai
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    def __init__(self, model="gpt-3.5-turbo") -> None:
        self.model = model
        self.client = openai.OpenAI()

    def __create_chat_completion(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content
    
    def get_response(self, command):
        messages=[
            {"role": "system", "content": "You are a vocal assistant. You have to answer in a simple, efficient and concise way. Your answer should not take more than 30 seconds to say out loud"},
            {"role": "user", "content": command},
        ]
        return self.__create_chat_completion(messages)
    
    def get_command_label(self, command):
        messages=[
            {"role": "system", "content": "You are a vocal assistant."},
            {"role": "system", "content": "Your role is to classify the user's command and return only the corresponding label."},
            {"role": "system", "content": "The labels are: to-do list, normal question"},
            {"role": "system", "content": "If you recognize the user's command as a to-do list request (for example), then return 'to-do list'."},
            {"role": "user", "content": command},
        ]
        return self.__create_chat_completion(messages)
    
    def get_audio_from_text(self, text):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )
        response.stream_to_file("temp.mp3")

