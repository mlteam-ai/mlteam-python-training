import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.memory = []
        self.memory_limit = 10

    def create_chat_completion(self, messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )

        return response["choices"][0]["message"]["content"]

    def get_response(self, command):
        messages=[
                {"role": "system", "content": "You are a vocal assistant. You have to answer in a simple, efficient and concise way. Your answer should not take more than 30 seconds to say out loud."},
        ]

        messages.extend(self.memory)
        messages.append(
            {"role": "user", "content": command}
        )

        assistant_reply = self.create_chat_completion(messages)

        if assistant_reply:
            self.memory.extend([
                {"role": "user", "content": command},
                {"role": "assistant", "content": assistant_reply}
            ])
            self.memory = self.memory[-self.memory_limit:]

        return assistant_reply
    
    def get_command_label(self, command):
        
        messages = [
                {"role": "system", "content": "You have to classify a command from the user."},
                {"role": "system", "content": "Your role is to classify the user's command and return only the corresponding label."},
                {"role": "system", "content": "The labels are : 'to-do list', 'weather', 'trivia', 'joke', 'normal'. The last label is for any unclassified command."},
                {"role": "system", "content": "If you recognize the user's command as a todo list request (for example),  then return 'to-do list'."},        
                {"role": "system", "content": "DO NOT answer anything else than the specified labels. If you don't know which one to return, return 'normal', even if the user says something like 'thank you'."},
                {"role": "user", "content": command}
        ]

        label = self.create_chat_completion(messages)
        return label
    
    def get_todo_command_label(self, command):

        messages = [
            {"role": "system", "content": "You are vocal assistant."},
            {"role": "system", "content": "You must classify the following command for a todo list functionnality, choose between one of these labels."},
            {"role": "system", "content": "Possible labels : add, remove, list, none."},
            {"role": "system", "content": "For example if the user says 'I want to go running tomorrow at 10 am', return 'add'."},
            {"role": "user", "content": command}
        ]

        label = self.create_chat_completion(messages)

        return label
    
    def generated_todo(self, command):
        messages = [
            {"role": "system", "content": "You are vocal assistant."},
            {"role": "system", "content": "The user is trying to add a task to their todo list, your job is to format their request into a concise task."},
            {"role": "system", "content": "For instance, if the user says 'I need to buy milk at 5 pm', you should rephrase it as 'Buy milk at 5 pm'."},
            {"role": "system", "content": "Ignore any word that are not part of the task itself."},
            {"role": "user", "content": command}
        ]

        todo = self.create_chat_completion(messages)
        return todo
    
    def get_approve_deny(self, command):

        messages = [
            {"role": "system", "content": "You are an assistant tasked with classifying user responses."},
            {"role": "system", "content": "The user will approve or deny a proposal."},
            {"role": "system", "content": "Detemine whether the user approves or denies."},
            {"role": "system", "content": "Return 'approve' or 'deny'."},
            {"role": "user", "content": command}
        ]

        decision = self.create_chat_completion(messages)

        return decision

    def recognize_todo(self, tasks, command):
        messages = [
            {"role": "system", "content": "Your task is to match the user's command to one of the lement of a todo list."},
            {"role": "system", "content": "The user wants to remove a specific task from his to-do list."},
            {"role": "system", "content": "Identify the task from their command and return it."},
            {"role": "system", "content": "If you find a task that matches his request, return the exact task text, nothing more. Else return 'none'."},
        ]

        for index, task in enumerate(tasks):
            messages.append(
                {"role": "system", "content": f"{index+1}: {task}"}
            )
        
        messages.append(
            {"role": "user", "content": command}
        )

        todo = self.create_chat_completion(messages)

        return todo
    
    def extract_information(self, info, command):

        messages = [
            {"role": "system", "content": "You are an AI assistant tasked with extracting specific information from user commands."},
            {"role": "system", "content": f"Extract the following detail: {info}"},
            {"role": "system", "content": f"If the user's message contains any '{info}', return only that detail."},
            {"role": "system", "content": f"If the user's message doesn't contain any '{info}', return only 'none'."},
            {"role": "system", "content": f"Remember, your response should only contain the {info} or 'none'."},
            {"role": "user", "content": command}
        ]

        extract = self.create_chat_completion(messages)

        return extract
    
    def rephrase(self, text):

        messages = [
            {"role": "system", "content": "You are a helpful rephrasing assistant. You need to rephrase a vocal assistant message in a deffirent, yet equivalent way."},
            {"role": "system", "content": "Keep the same meaning and average length, but change the structure and words when possible."},
            {"role": "system", "content": "Try to avoid using uncommon or complicated words in the rephrased version, keep it simple."},
            {"role": "system", "content": "Keep in mind that the text should be simple and concise, and shouldn't take more than 20 seconds to say out loud."},
            {"role": "user", "content": text},
        ]

        rephrased_command = self.create_chat_completion(messages)

        return rephrased_command
    
    def check_trivia_answer(self, correct_answer, user_answer):

        messages = [
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "system", "content": "You will be given an answer from a user to a trivia question."},
            {"role": "system", "content": "The user might use phrases like 'I think', 'Maybe', 'I believe', etc..."},
            {"role": "system", "content": "But you need to focus on the main content of the answer."},
            {"role": "system", "content": "If the user's answer is correct, simply reply with 'Correct'. If it is not, reply with 'Incorrect'. Reply with the exact same spelling. Don't add a '.' at the end for example."},
            {"role": "user", "content": f"The correct answer to a trivia question is '{correct_answer}'. The person answered '{user_answer}'. Is the person's answer correct ?"},

        ]

        verdict = self.create_chat_completion(messages)
        return verdict

