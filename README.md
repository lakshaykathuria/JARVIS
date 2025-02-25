# J.A.R.V.I.S. - Personal Voice Assistant

J.A.R.V.I.S. is a Python-based personal voice assistant capable of performing various tasks, such as searching the web, playing YouTube videos, sending WhatsApp messages, opening applications, and more.

## Prerequisites
Before running the main script, ensure you have the required Python libraries installed. Use the following command to install them:

```sh
pip install pyttsx3 speechrecognition datetime pywhatkit webbrowser pyautogui time os openai AppOpener
```

## Features
- **Voice Recognition**: Recognizes voice commands and responds accordingly.
- **Speech Output**: Uses text-to-speech (TTS) to provide spoken responses.
- **Google Search**: Searches the web for a given query.
- **YouTube Control**: Plays videos based on user requests.
- **ChatGPT Integration**: Answers queries using OpenAI's API.
- **System Commands**: Shutdown, restart, and application management.
- **Date & Time**: Provides the current date and time.
- **Messaging**: Sends WhatsApp messages.
- **Application Management**: Opens and closes apps like Notepad, Calculator, WhatsApp, and Telegram.

## How to Run
1. Install the required libraries using the `pip install` command above.
2. Run the script:

   ```sh
   python main.py
   ```

3. Speak commands when prompted.

## Voice Commands
Here are some example commands you can use:
- "Jarvis, play [song name] on YouTube"
- "Jarvis, search [query] on Google"
- "Jarvis, what is the time?"
- "Jarvis, shutdown the system"
- "Jarvis, send a message on WhatsApp"
- "Jarvis, open Notepad"
- "Jarvis, take a note"

## Notes
- Ensure your microphone is working properly for accurate speech recognition.
- The WhatsApp messaging feature requires the app to be installed and logged in.
- ChatGPT integration requires an OpenAI API key (ensure you configure it properly).

## Author
Developed by Lakshay



