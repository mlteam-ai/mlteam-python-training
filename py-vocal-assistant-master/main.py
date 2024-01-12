from speech_processing import SpeechProcessing
from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager
from weather_agent import WeatherAgent
from trivia_agent import TriviaAgent
from jokes_agent import JokesAgent
import time

class MainApp:
    def __init__(self):
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()
        self.weather_agent = WeatherAgent()
        self.trivia_agent = TriviaAgent()
        self.jokes_agent = JokesAgent()

    def run(self):

        while True:
            
            if self.speech_processor.listen_for_wakeword():
                self.speech_processor.speak("Hi ! How can I assist you today ?")

                while True:
                    
                    command = self.speech_processor.listen(timeout=7)

                    if command == "":
                        break                   
                    elif command is not None:

                        label = self.command_processor.handle_command(command)

                        if label == "to-do list":
                            self.todo_manager.handle_command(command)
                        elif label == "weather":
                            self.weather_agent.handle_command(command)
                        elif label == "trivia":
                            self.trivia_agent.handle_command(command)
                        elif label == "joke":
                            self.jokes_agent.handle_command(command)
                        else:
                            gpt_answer = self.openai_agent.get_response(command)
                            print(f"ChatGPT Answered: {gpt_answer}")
                            self.speech_processor.speak(gpt_answer)
                    time.sleep(0.1)
            time.sleep(0.1)

if __name__ == "__main__":
    app = MainApp()
    app.run()