import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from openai_agent import OpenAIAgent

class SpeechProcessing:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.openai_agent = OpenAIAgent()

    def listen_for_wakeword(self):
        wakeword = "hello my friend"
        with sr.Microphone() as micinput:
            self.recognizer.adjust_for_ambient_noise(micinput, duration=1)      
            try:
                print("Waiting for wake word...")
                audio = self.recognizer.listen(micinput, timeout=5)
                if audio: 
                    text = self.recognizer.recognize_google(audio)
                    if text.lower() == wakeword:
                        return True
            except Exception:
                return False
        return False

    def listen(self, timeout=5):
        with sr.Microphone() as micinput:
            self.recognizer.adjust_for_ambient_noise(micinput, duration=1)
            
            text = ""
            audio = None
            try:   
                print("Listening...")
                self.play_sound()
                audio = self.recognizer.listen(micinput, timeout)
            except sr.WaitTimeoutError as error:
                print("WaitTimeoutError occurred:", error)
                return text
            except Exception as error:
                print("Exception occurred:", error)
                return text

            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f"User said: {text}")
            except sr.UnknownValueError as error:
                pass
            except sr.RequestError as error:
                print("RequestError occurred:", error)
            except Exception as error:
                print("Exception occurred:", error)
            return text
        
    def speak(self, text, rephrase=True):
        if rephrase:
            rephrased_text = self.openai_agent.rephrase(text)
            if rephrased_text and rephrased_text != "":
                text = rephrased_text
        temp_audio_file = "temp.mp3"
        self.openai_agent.get_audio_from_text(text, temp_audio_file)
        audio = AudioSegment.from_file(temp_audio_file, format="mp3")
        play(audio)

    def play_sound(self):
        sound_file = "listen_sound.mp3"
        audio = AudioSegment.from_file(sound_file, format="mp3")
        play(audio)