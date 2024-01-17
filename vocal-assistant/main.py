from speech_processing import SpeechProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager
from weather_agent import WeatherAgent
import time
from trivia_agent import TriviaAgent
from jokes_agent import JokesAgent

class MainApp:
    def __init__(self) -> None:
        self.speech_processor = SpeechProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()
        self.weather_agent = WeatherAgent()
        self.trivia_agent = TriviaAgent()
        self.jokes_agent = JokesAgent()
    
    def run(self):
        while True:
            awake = self.speech_processor.listen_for_wakeword()
            if awake:
                self.speech_processor.speak("Hi! How can I assist you today?")
                while True:
                    command = self.speech_processor.listen(timeout=7)
                    if command == "":
                        break # Will break the inner while loop and start to listen for wake word
                    else:
                        label = self.openai_agent.get_command_label(command)
                        print("Command label recognized by GPT:", label)

                        if label == "to-do list":
                            self.todo_manager.handle_command(command)
                        elif label == "weather":
                            self.weather_agent.handle_command(command)
                        elif label == "trivia":
                            self.trivia_agent.handle_command(command)
                        elif label == "joke":
                            self.jokes_agent.handle_command(command)
                        elif label == "normal question":
                            gpt_response = self.openai_agent.handle_command(command)
                            self.speech_processor.speak(gpt_response)
                    time.sleep(0.1)
            time.sleep(0.1)


if __name__ == "__main__":
    app = MainApp()
    app.run()