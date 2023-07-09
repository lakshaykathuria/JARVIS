import pyttsx3
import speech_recognition as sr
from datetime import datetime
import pywhatkit
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")

    elif hour >= 18 and hour < 24:
        speak("Good Evening Boss")
    print("I am Jarvis, Sir Plz tell me how may i help you")
    speak("I am Jarvis, Sir Plz tell me how may i help you")

        
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening....")
            audio = r.listen(source)
            r.pause_threshold = 1
            query = r.recognize_google(audio, language = 'en-us')
            print("user said: ", query,"\n")
            return query
            
        except Exception as e:
            print("Please Say That Again")
            takecommand()
            return True
                

def wiki(query):
    
    speak("searching....")
    query = query.replace("wikipedia","")
    results = wikipedia.search(query)
    print(results)
    speak(results)

def google(query):
   
    speak("searching....")
    query = query.replace("on Google","")
    query = query.replace("search the","")
    query = query.replace("search","")
    query = query.replace("Google","")
    query = query.replace("Please","")

    results = pywhatkit.search(query)

def youtube(query):
    
    speak("Opening Youtube")
    query = query.replace("on youtube","")
    query = query.replace("play","")
    pywhatkit.playonyt(query)

wishMe()
query = takecommand() 
if 'YouTube' in query:
    youtube(query)
elif 'Google' in query:
    google(query)
elif 'Wikipedia' in query:
    wiki(query)
