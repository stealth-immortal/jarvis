

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" I am Jarvis Sir, Please tell me how may I help you..")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query

#def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('youremail@gmail.com', 'your-password')
    #server.sendmail('youremail@gmail.com', to, content)
    #server.close()
if __name__ == '__main__':
    wishMe()
    #while True:(4 continues listening enable this)
    if 1:
        query = takecommand().lower()

    # logic to executing tasks based on  query
    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia.")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open github' in query:
        webbrowser.open("github.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")


    elif 'play music' in query:
        music_dir = 'D:\\songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:&S")
        speak(f" Sir, the time is {strTime}")

    elif 'open pycharm' in query:
        codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.2\\bin"
        os.startfile(codePath)

    elif 'open code' in query:
        codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    #elif 'email to sinu' in query:
     #   try:

      #      speak("What should I say?")
       #     content = takecommand()
        #    to = "sinuyourEmail@gmail.com"
         #   sendEmail(to, content)
          #  speak("Email has been sent!")
        #except Exception as e:
         #   print(e)
          #  speak("Sorry yaar sinu. I am not able to send this email")