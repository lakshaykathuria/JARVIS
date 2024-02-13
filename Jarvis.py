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

def currenttime():
    time = datetime.now()
    print(time.strftime('%I:%M:%S %p'))
    speak(time.strftime('%I:%M:%S %p'))

def today():
    today = datetime.today()
    day = today.strftime("%A")
    date = today.strftime("%B %d, %Y")
    print("Today is :",day + " , " + date )
    speak("Today is :",day + " , " + date )


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
    client = OpenAI()
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

def  restart():
    os.system('restart /r /t 1')

def sleep():
    os.system('powercfg /hibernate off')

def send_whatsapp_message():
    speak("please Enter the recipient's phone number with country code")
    pyautogui.click(x=900, y=900)
    recipient = input("Enter the recipient's phone number with country code: ")
    speak('Enter the message you want to send: ')
    message = input("Enter the message you want to send: ")
    open('whatsapp')
    time.sleep(4)
    pyautogui.click(x=200, y=155)
    pyautogui.typewrite(recipient)
    time.sleep(3)
    pyautogui.click(x=250, y=250)
    time.sleep(2)
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    print("Message sent successfully!")
    speak("Message sent successfully!")
    
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

            
            elif 'calculator' in query:
                open('calculator')
                break

            elif 'time' in query:
                currenttime()
            elif 'date' in query or 'day' in query:
                today()
            elif 'shutdown ' in query:
                shutdown()
            elif  'restart ' in query:
                restart()


            elif 'send message' in query or 'send a message' in query or 'send a message on whatsapp'in query:
                send_whatsapp_message()
                break

            elif 'bye' in query:
                break
            else:
                chatgpt(query)

if __name__ == "__main__":
    wishMe()
    jarvis()


    
# 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
    