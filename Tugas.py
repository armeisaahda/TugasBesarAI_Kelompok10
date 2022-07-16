import pyttsx3 #udah install
import speech_recognition as sr #udah install
import datetime #udah install
import wikipedia #udah install
import webbrowser
import os
import smtplib

print("initializing Ultraman")

MASTER = "tria"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")

# microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        query = None

    return query

# main start here
speak("Hello my name is Ultraman, i can help you!")
wishMe()
query = takeCommand()

#logic for tasks as per query
if "wikipedia" in query.lower():
    speak("searching wikipedia..")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif "open youtube"  in query.lower():
    url = "youtube.com"
    
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "open google" in query.lower():
    url = "google.com"
    
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)


elif "open time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak("(MASTER) the time is(strtime)")
