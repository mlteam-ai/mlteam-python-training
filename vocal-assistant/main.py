from speech_processing import SpeechProcessing
from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager

class MainApp:
    def __init__(self) -> None:
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()
    def run(self):
        while True:
            command = self.speech_processor.listen()

if __name__ == "__main__":
    app = MainApp()
    app.run()