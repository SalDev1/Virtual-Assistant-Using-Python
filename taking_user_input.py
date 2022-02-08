import speech_recognition as sr
from random import choice
from utils import opening_text
from speech_engine import speak
from datetime import datetime

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
        # print("You said" + query)
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


take_user_input();