import pyttsx3
from decouple import config
from datetime import datetime
from os_ops import open_calculator,open_camera,open_cmd,open_notepad, open_spotify , open_visual_studio_code
import speech_recognition as sr
from random import choice
from utils import opening_text
from online_ops import play_on_youtube, search_on_wikipedia , search_on_google


# Making use of environment variables
USERNAME = config('USER');
BOTNAME = config('BOTNAME');

# Fetching out the sapi5 (Microsoft Speech Recongition)
engine = pyttsx3.init('sapi5');

# Set Rate
engine.setProperty('rate' ,  190);

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices');
# We are setting the voice of the assistant to the female
engine.setProperty('voice' , voices[1].id);

# print(voices);

# Text to Speech Conversion
def speak(text):
    engine.say(text);
    engine.runAndWait();

speak("Hello There");

def greet_user():
    # Greets the user according to the time
    hour = datetime.now().hour
    if(hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif(hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif(hour >= 16 and hour < 19):
        speak(f"Good evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you ?")


def take_user_input():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing')
        # This API will try to recognize the speech that we are saying
        query = r.recognize(audio)

        if not 'exit' in query or 'stop' in query :
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6 :
                speak("Good night sir , take care!")
            else:
                speak("Have a good day sir !")
            exit()
    except Exception:
        speak("Sorry I could not understand . Could you please say that again ?")
        query = 'None'
    return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()
        
        elif 'open spotify' in query:
            open_spotify()
    
        elif'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        
        elif 'open calculator' in query :
            open_calculator()
        
        elif('open camera') in  query:
            open_camera()

        elif('open visual studio code') in  query:
            open_visual_studio_code()

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia , sir ?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f'According to Wikipedia , {results}')
            speak("For your convenience , I am printing it on the screen")
            print(results)

        elif 'search on google' in  query:
            speak("What do you want to search on Google , sir ? ")
            query = take_user_input().lower()
            search_on_google(query)

        elif 'youtube' in query:
            speak("What do you want to play on Youtube, sir?")
            video = take_user_input().lower()
            play_on_youtube(video)
            
        elif("stop") in query:
            exit()