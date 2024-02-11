import pyttsx3
import speech_recognition as sr
from datetime import datetime
import pywhatkit
import webbrowser
import pyautogui
import time
import  os
from openai import OpenAI
from AppOpener import open
from AppOpener import close

client = OpenAI()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening....")
            audio = r.listen(source)
            r.pause_threshold = 1
            query = r.recognize_google(audio, language = 'en-in')
            print("user said: ", query,"\n")
            return query
            
        except Exception as e:
            print("Please Say That Again")
            return takecommand()
            
                
def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning ")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ")

    elif hour >= 16 or hour < 6:
        speak("Good Evening ")
    print("I am Jarvis, Please tell me how may i help you")
    speak("I am Jarvis, Please tell me how may i help you")


def google(query):
   
    speak("searching....")
    query = query.replace("on Google","")
    query = query.replace("search the","")
    query = query.replace("search","")
    query = query.replace("Google","")
    query = query.replace("Please","")

    results = pywhatkit.search(query)

def youtube(query):
    if  "play" or  "watch" in query:
        query = query.replace("play","").replace("watch","").strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        time.sleep(5) 
        pyautogui.click(x=760, y=300)

def chatgpt(query):
    query = query.replace("jarvis","")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": query}
            ]
        )
    print(completion.choices[0].message.content)
    speak(completion.choices[0].message.content)

def  shutdown():
    os.system('shutdown /s /f')

def jarvis():
    while True:
        query = takecommand().lower()
        
        if query:
            query = query.replace("jarvis",'')

            if 'play' in query:
                youtube(query)
                speak('playing')
                
                break

            elif 'google' in query or 'search' in query:
                google(query)
                break

            elif 'open whatsapp' in query or 'open the whatsapp' in query:
                open("whatsapp")
            elif 'close whatsapp' in query or 'close the whatsapp' in query:
                close("whatsapp")

            elif 'open telegram' in query or 'open the telegram' in query:
                open("telegram")
            elif 'close telegram' in query or 'close the telegram' in query:
                close("telegram")
            
            
            else:
                chatgpt(query)

if __name__ == "__main__":
    wishMe()
    jarvis()


    
# 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
    