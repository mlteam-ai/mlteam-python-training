from openai_agent import OpenAIAgent
from speech_processing import SpeechProcessing
from command_processing import CommandProcessing

class TodoManager:
    def __init__(self) -> None:
        self.openai_agent = OpenAIAgent()
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.tasks = []
    
    def add_to_list(self, item):
        todo = self.openai_agent.generate_todo(item)
        print(f"Todo to be added: {todo}")
        if todo:
            self.tasks.append(todo)
            self.speech_processor.speak(f"Successfully added '{todo}' to your task list !")
        for task in self.tasks:
            print(task)

    def remove_from_list(self, command):
        item = self.openai_agent.recognize_todo(self.tasks, command)
        if item in self.tasks:
            self.speech_processor.speak(f"Do you want to remove '{item}' from your to-do list?")
            decision = self.speech_processor.listen()
            decision = self.command_processor.get_approve_deny(decision)
            if decision == "approve":
                self.tasks.remove(item)
                self.speech_processor.speak(f"'{item}' is successfully removed from your to-do list!")
            else:
                self.speech_processor.speak(f"Okay! I won't remove '{item}' from your to-do list!")
        else:
            self.speech_processor.speak("I could not recognize the task! Please try again")
    def list_tasks(self):
        text = "Here is what is in your todo list:"
        for index, todo in enumerate(self.tasks):
            text += f"{index + 1}: {todo}. "
        self.speech_processor.speak(text)

    def handle_command(self, command):
        label = self.openai_agent.get_todo_command_label(command)
        print(f"Command: {command}, Label: {label}")

        if label == "add":
            self.add_to_list(command)
        elif label == "remove":
            self.remove_from_list(command)
        elif label == "list":
            self.list_tasks()
        else:
            self.speech_processor.speak("I could not understand your command! Please try again")