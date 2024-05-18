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
import subprocess


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
    speak(f"Today is : {day},  {date}")


def google(query):
    speak("searching....")
    query = query.replace("on google","")
    query = query.replace("search the","")
    query = query.replace("search","")
    query = query.replace("google","")
    query = query.replace("please","")

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
    os.system('shutdown /s /f /t 1')

def  restart():
    os.system('shutdown /r /t 1')

def stop():
    pyautogui.hotkey('alt', 'f4')


def send_whatsapp_message():
    speak("please Enter the recipient's phone number")
    pyautogui.click(x=900, y=900)
    recipient = takecommand()
    speak('Enter the message you want to send: ')
    message = takecommand()
    open('whatsapp')
    time.sleep(2)
    pyautogui.click(x=200, y=155)
    pyautogui.typewrite(recipient)
    time.sleep(2)
    pyautogui.click(x=250, y=250)
    time.sleep(2)
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    print("Message sent successfully!")
    speak("Message sent successfully!")

def updates():
    subprocess.run(['control', '/name', 'Microsoft.WindowsUpdate'])
    time.sleep(2)
    pyautogui.click(x=1700, y=200)

def note():
    open('notepad')
    speak('what do you wanna note')
    topic = takecommand()
    pyautogui.typewrite(topic)
    
def jarvis():
    while True:
        query = takecommand().lower()
        
        if query:
            query = query.replace("jarvis",'')

            if 'play' in query:
                youtube(query)
                speak('playing')
                
            elif 'close youtube' in query:
                stop()

            elif 'google' in query or 'search' in query:
                google(query)
                
            elif 'close google' in query:
                stop()


            elif 'yourself' in query:
                print("I'm an artificial intelligence developed by Lakshay called JARVIS. My purpose is to assist and engage in conversation with users like you.")
                speak("I'm an artificial intelligence developed by Lakshay called JARVIS. My purpose is to assist and engage in conversation with users like you.")

            elif 'open whatsapp' in query or 'open the whatsapp' in query:
                open("whatsapp")
            elif 'close whatsapp' in query or 'close the whatsapp' in query:
                close("whatsapp")


            elif 'open telegram' in query or 'open the telegram' in query:
                open("telegram")
            elif 'close telegram' in query or 'close the telegram' in query:
                close("telegram")

            
            elif 'open calculator' in query:
                open('calculator')
            elif'close calculator' in query:
                stop()

            elif 'open settings' in query:
                open('settings')
            elif 'close setting' in query:
                stop()

            elif 'close notepad' in query:
                stop()
            elif 'note' in query:
                note()

            elif 'time' in query:
                currenttime()
            elif 'shutdown' in query:
                shutdown()
                break
            elif  'restart' in query:
                restart()
                break
            elif 'update' in query or  'updates' in query:
                updates()

            elif 'close update' in query or 'stop updating' in query:
                stop()

            elif 'date' in query or 'day' in query:
                today()

            elif 'send message' in query or 'send a message' in query or 'send a message on whatsapp'in query:
                send_whatsapp_message()
                

            elif 'bye' in query or 'exit' in query or 'stop' in query:
                break
            else:
                chatgpt(query)

if __name__ == "__main__":
    wishMe()
    jarvis()


    

    
