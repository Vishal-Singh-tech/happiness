import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning !")
    elif hour>=12 and hour <18:
        speak("good afternoon!")
    else:
        speak("good evening")
    speak("sir i m kookku. how may i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 2000
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
            #print(e)

        print("say that again please...") 
        return "None"
    return query


if __name__  ==  "__main__":
    wishMe()
    if 1:
    #while True:
        
        query = takecommand().lower()
       
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
           music_dir = 'D:\\my bad\\favorite song'
           song = os.listdir(music_dir)

           os.startfile(os.path.join(music_dir,song[0]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open visual studio code' in query:
            codepath="C:\\Users\\visal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)



