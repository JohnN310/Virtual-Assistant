import warnings 
import pygame
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell

warnings.filterwarnings("ignore")

# Suppress welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Initialize pygame
pygame.init()

# Initialize pygame mixer
pygame.mixer.init()

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 for female, 0 for male
engine.setProperty('rate', 150)  # Adjust the rate value to control the speech speed
assistant_name="charlotte"

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)
    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    
    except sr.RequestError as ex: 
        print("Request error from Google Speech Recognition" + ex)

    return data


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio_path = "Audio.mp3"
    tts.save(audio_path)

    # Use pygame to play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Cleanup
    pygame.mixer.quit()
    os.remove(audio_path)

def call(text):
    action_call=assistant_name

    text=text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now=calendar.day_name[date_now.weekday()]
    month_now=now.month
    day_now=now.day
    
    months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
    ]

    ordinals=[
    "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",
    "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
    "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."
    return "Hi"

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            # Combine the first and last names, handling potential formatting issues
            person_name = list_wiki[i + 2] + " " + list_wiki[i + 3]
            return person_name.strip()  # Remove leading and trailing spaces

def shutdown_sound():
    # Initialize pygame
    pygame.init()
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.Sound("shutdown.mp3").play()
    pygame.time.delay(2000)

def startup_sound():
    # Initialize pygame
    pygame.init()
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.Sound("startup.mp3").play()
    pygame.time.delay(2000)

# Main program
count=0
startup_sound()
boo=False
while True:
    try:
        text=rec_audio()
        speak=" "
        if call(text) or boo:
            speak = speak + say_hello(text)
            boo=True
             
            if "how" not in text and ("date" in text or "day" in text or "month" in text):
                get_today = today_date()
                speak = get_today

            elif "time" in text:
                now = datetime.datetime.now()
                
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m."
                    hour = now.hour-12
                else:
                    meridiem = "a.m."
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = "It is " + str(hour) + ":" + minute + " " + meridiem

            elif "who is" in text: 
                    person =wiki_person(text)
                    wiki = wikipedia.summary(person, sentences = 2)
                    speak = wiki

            elif "who are you" in text:
                speak= "Hello, I am "+ assistant_name+ " your virtual assistant. I am here to make your life easier. Tôi có thể nói tiếng việt, puedo hablar español, and many other languages. Let me know when you need help with anything"

            elif "your name" in text:
                speak = "my name is "+assistant_name

            elif "who am I" in text: 
                 speak = "you are probably a human"

            elif "how are you" in text: 
                speak = "I am fine, thank you. How are you?"
            
            elif "fine" in text or "good" in text:
                speak = "It's good to know that you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = "Opening Google Chrome"
                    os.startfile(
                        r"C://Program Files//Google//Chrome//Application//chrome.exe"
                    )
                
                elif "word" in text.lower():
                    speak = "Opening Microsoft Word"
                    os.startfile(
                        r"C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = "Opening Microsoft Excel"
                    os.startfile(
                        r"C://Program Files//Microsoft Office//root//Office16//EXCEL.EXE"
                    )
                
                elif "vs code" in text.lower():
                    speak = "Opening vs code"
                    os.startfile(
                        r"C://Users//anhkh//AppData//Local//Programs//Microsoft VS Code//Code.exe"
                    )

                elif "youtube" in text.lower():
                    speak = "Openning youtube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = "Openning google"
                    webbrowser.open("https://google.com/")
                
                else:
                    speak = "application not found"

            elif "search" in text.lower() and "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind+1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query="+"+".join(search)
                )
                speak = "Opening and searching on youtube"
        
            elif "search" in text.lower() or "google" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind+1:]
                webbrowser.open(
                    "https://www.google.com/search?q="+"+".join(search)
                )
                speak = "Searching "+str(search)+" on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r"C://Users//anhkh//Downloads//GitHub//Python_Voice Assistant//Backgrounds"
                list_img=os.listdir(img)
                img_choice=random.choice(list_img)
                randomImg=os.path.join(img, img_choice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = "Changed background sucessfully"

            elif "play music" in text or "play song" in text:
                music_dir = r"C://Users//anhkh//Downloads//GitHub//Python_Voice Assistant//Music Folder"
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                randomSong = os.path.join(music_dir, d)
                playsound.playsound(randomSong)

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(confirm = True, show_progress=False, sound=True)
                speak = "Emptied recycle bin"

            elif "go to sleep" in text:
                shutdown_sound()
                break 
        else:
            if count==0:
                speak = "Sorry, I don't get that. Can you say it one more time?"                    
                count+=1
            else:
                speak = "Sorry, I don't know that, I need to be programmed to understand this. What else can I help you with?"           
        response(speak)

    except:
        response("I don't know that")
        break


