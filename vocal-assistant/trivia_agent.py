import requests
from speech_processing import SpeechProcessing
from openai_agent import OpenAIAgent
import random

trivia_base_url = "http://the-trivia-api.com/v2/questions"

class TriviaAgent:
    def __init__(self) -> None:
        self.speech_processor = SpeechProcessing()
        self.openai_agent = OpenAIAgent()

    def get_question(self, limit=1):
        try:
            params = {
                "limit": limit,
            }
            response = requests.get(trivia_base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                question_data = {
                    "category": data[0]["category"],
                    "question": data[0]["question"]["text"],
                    "correct": data[0]["correctAnswer"],
                    "incorrects": data[0]["incorrectAnswers"],
                }
                return question_data
        except Exception as error:
            print("An exception occured:", error)
        return None
    
    def handle_command(self, command):
        self.speech_processor.speak("Do you want me to ask you a trivia question?")
        decision = self.speech_processor.listen()
        decision = self.openai_agent.get_approve_deny(decision)
        if decision == "approve":
            self.start_trivia()
        else:
            self.speech_processor.speak("Ok, it is totally fine, let me know if you need help for anything.")

    def start_trivia(self):
        question = self.get_question()
        print("Correct answer:", question["correct"])
        possible_answers = []
        possible_answers.append(question["correct"])
        possible_answers.extend(question["incorrects"])
        random.shuffle(possible_answers)
        text = f"Category of the question: {question["category"]}. Here is the question: {question["question"]}? Here is the possible answers: "
        for index, answer in enumerate(possible_answers):
            text += f"{index + 1}: {answer}, "
        self.speech_processor.speak(text, rephrase=False)
        user_answer = self.speech_processor.listen()
        is_correct_answer = self.openai_agent.check_trivia_answer(correct_answer=question["correct"], user_answer=user_answer)
        if is_correct_answer:
            self.speech_processor.speak("Congratulations! This is the right answer.")
        else:
            self.speech_processor.speak("This is not the right answer. You can try a new question if you want.")