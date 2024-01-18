# Vocal Assistant Project
This project is based on the content of a course in Udemy called [5-in-1 Mega Course: Python, Javascript, React JS, CSS, AI](https://deliveryhero.udemy.com/course/python-ai-crashcourse/learn/lecture/41713364#overview).

# Overview
Vocal assistant continously listens the user's microphone. When they speak, it classifies the command as 'to-do list', 'weather', 'trivia', 'joke', 'normal question'. Then it interacts with the user in a vocal way. For each tyep of command, it does the following:
* **'to-do list'**: You can add, remove items to your to-do list. You can list the items in your to-do list.
* **'weather'**: You can ask the whether in a specific location/city. For this, it is integrated to [weather api](https://www.weatherapi.com/).
* **'trivia'**: It can ask you a trivia question, listen your response and tell you if it was correct or not. For this, it is integrated to [the trivia api](https://the-trivia-api.com/).
* **'joke'**: It tells you a joke. For this, it is integrated to [API ninjas](https://api-ninjas.com/).
* **'normal question'**: It gets your question and replies back using [Chat Completions API of Open AI](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) with gpt-3.5-turbo as the model.

# Installation

## 1. Setting up '.env' file
* Create a '.env' file in the [vocal_assistant](.) folder.
* You need to subscribe to OpenAI, configure your billing settings, get your API key and put it in '.env' file with 'OPENAI_API_KEY' name.
* You need to subscribe to [weather api](https://www.weatherapi.com/), choose the free plan, get your API key and put it in '.env' file with 'WEATHER_API_KEY' name.
* You need to subscribe to [API ninjas](https://api-ninjas.com/), choose the free plan, get your API key and put it in '.env' file with 'APININJA_API_KEY' name. 
* If any of your API keys contains an equal sign (=), you need to enclose it in quotes(").

Here is a sample '.env' file:
```
OPENAI_API_KEY=sk-nhxWyKOMyw46OyKOM6eZxKoEyKOMs31XK5se
WEATHER_API_KEY=2eb0a3b0fdb0fb00b8b0
APININJA_API_KEY="goYo94LHFYo9FHEPYYo9o9Q6nQ==kNey2rsUyey2rey2"
```

## 2. Installing the dependencies
Open a terminal window, change your working directory to [vocal-assistant](.), run the following commands:
```sh
    chmod +x setup.sh
    ./setup.sh
```

# Execution
To start your vocal assistant run the following command in [vocal-assistant](.) folder.
```sh
    python3 main.py
```