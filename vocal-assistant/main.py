from speech_processing import SpeechProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager
from weather_agent import WeatherAgent

class MainApp:
    def __init__(self) -> None:
        self.speech_processor = SpeechProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()
        self.weather_agent = WeatherAgent()
    
    def run(self):
        while True:
            command = self.speech_processor.listen()
            if command != "":

                label = self.openai_agent.get_command_label(command)
                print("Command label recognized by GPT:", label)

                if label == "to-do list":
                    self.todo_manager.handle_command(command)
                elif label == "weather":
                    self.weather_agent.handle_command(command)
                elif label == "normal question":
                    gpt_response = self.openai_agent.handle_command(command)
                    self.speech_processor.speak(gpt_response)


if __name__ == "__main__":
    app = MainApp()
    app.run()