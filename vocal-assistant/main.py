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
            if command != "":

                label = self.command_processor.handle_command(command)
                print("Command label recognized by GPT:", label)

                if label == "to-do list":
                    print("Do something with Todo manager")
                    self.openai_agent.get_audio_from_text("Do something with Todo manager")
                    self.speech_processor.speak()
                elif label == "normal question":
                    gpt_response = self.openai_agent.get_response(command)
                    print("ChatGPT answered:", gpt_response)
                    self.openai_agent.get_audio_from_text(gpt_response)
                    self.speech_processor.speak()

if __name__ == "__main__":
    app = MainApp()
    app.run()