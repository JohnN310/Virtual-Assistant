from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
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
import pyjokes
import subprocess
import smtplib
import requests
import json
import wolframalpha

warnings.filterwarnings("ignore")

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
        print(" ")
    
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
    return " "

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

def note(text):
    file_name = "note"+"-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])


def send_email(to, content):
    sever=smtplib.SMTP("smtp.gmail.com", 587)
    sever.ehlo()
    sever.starttls()
    server.login("email", "password")
    sever.sendmail("email", to, content)
    sever.close()

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
def google_calendar(num):
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=num,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      response("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    response("Getting "+ str(num) + " events: ")
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      end = event["end"].get("dateTime", event["end"].get("date"))
      start=start.split("T")
      end = end.split("T")
      response("On " + start[0])
      response("From "+start[1].split("-")[0]+" to "+end[1].split("-")[0])
      response(event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")

def wolfram_alpha_query(query):
    base_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "format": "plaintext",
        "output": "JSON",
        "appid": "JXWQV9-P9PQGYLW55",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

# Main program
count=0
startup_sound()
boo=False
while True:
    try:
        text=rec_audio()
        speak=" "
        if call(text) or boo:
            speak = say_hello(text)
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

            # elif "who is" in text: 
            #         person =wiki_person(text)
            #         wiki = wikipedia.summary(person, sentences = 2)
            #         speak = wiki

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
                img = r"C://Users//anhkh//OneDrive//GitHub//Python_Voice Assistant//Backgrounds"
                list_img=os.listdir(img)
                img_choice=random.choice(list_img)
                randomImg=os.path.join(img, img_choice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = "Changed background sucessfully"

            elif "play music" in text or "play a song" in text or "song" in text:
                music_dir = r"C://Users//anhkh//OneDrive//GitHub//Python_Voice Assistant//Music Folder"
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                randomSong = os.path.join(music_dir, d)
                playsound.playsound(randomSong)
                response("How was it? Do you like the song?")
                text1=rec_audio()
                if "yes" in text1: 
                    speak = "That's good to hear. What else can I help you with?"
                if "no" in text1: 
                    speak = "Ooh, I'll try better next time. What else can I help you with?"

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(confirm = True, show_progress=False, sound=True)
                speak = "Emptied recycle bin"

            elif "note" in text or "take notes" in text or "remember" in text:
                response("What would you like me to take notes of?")
                note_text= rec_audio()
                note(note_text)
                speak = "Notes taken successfully"

            elif "jokes" in text or "joke" in text: 
                speak = pyjokes.get_joke() 
            #add more to this part 
            
            elif "where is" in text: 
                ind = text.lower().split().index("is")
                location = text.split()[ind+1:]
                speak = "This is where " + str(location) + " is."
                webbrowser.open("https://www.google.com/maps/place/" +"".join(location))

            elif "email to" in text or "write an email" in text: 
                try: 
                    response("What should I say?")
                    content = rec_audio()
                    response("Enter the receiver's email address: ")
                    to = input("Enter: ")
                    send_email(to, content)
                    speak = "Email has been sent"
                except Exception as e:
                    print(e)
                    response("Unable to send the email")

            elif "weather" in text: 
                key="e4ba798f88bdd74531428e6735ebe711"
                ind = text.lower().split().index("in")
                city = text.split()[ind+1:]
                endpoint = f"http://api.weatherstack.com/current?access_key={key}&query={city}"
                weatherstack_response = requests.get(endpoint)
                if weatherstack_response.status_code == 200:
                    data = weatherstack_response.json()
                    response("The weather in " + str(city) +", " +str(data["location"]["country"]) + " is " + str(data["current"]["temperature"])+ " Celcius degrees. The sky is currently "+ str(data["current"]["weather_descriptions"][0])+" with humidity of " + str(data["current"]["humidity"]))
                    response("Do you want to hear more?")
                    text1= rec_audio()
                    if "yes" in text1:
                        speak = "In "+str(city)+", the windspeed is "+str(data["current"]["wind_speed"])+", the pressure is "+str(data["current"]["pressure"])+" and the UV index is "+str(data["current"]["uv_index"])+". What else can I help you with?"
                    if "no" in text1:
                        speak = "Great. What else can I help you with?"

            elif "news" in text or "News" in text: 
                url = ('https://newsapi.org/v2/everything?q=us&from=2023-11-09&sortBy=publishedAt&apiKey=3e08910778ea403aa5649faab8fbb916')
                try: 
                    news_response = requests.get(url)

                except:
                    response("Please check your connection")
                
                news = json.loads(news_response.text)

                for new in news["articles"]:
                    response(str(new["title"]))
                    response(str(new["description"]))

                speak = "what else can I help you with?"
            # control the news flow

            elif "calendar" in text or "events" in text:
                liststr = text.lower().split()
                if "events" in text:
                    num = liststr[-2]
                else:
                    num = 10
                google_calendar(num) 
                speak = "What else can I help you with?"

            elif "what is" in text or "who is" in text or "calculate" in text:
                result = wolfram_alpha_query(text)
                # Process the result
                if result["queryresult"]["success"]:
                    pods = result["queryresult"]["pods"]
                    if "subpods" in pods[1]:
                        subpods = pods[1]["subpods"]
                        for i in range(len(pods)):
                            if pods[i].get("title") == "Result" or pods[i].get("title") == "Decimal approximation":
                                speak = "The answer is "+ pods[i]["subpods"][0].get("plaintext")
                            if pods[i].get("title") == "Wikipedia summary":
                                speak = "This is what I found on wikipedia "+pods[i]["subpods"][0].get("plaintext").split(". ")[0]+". "+pods[i]["subpods"][0].get("plaintext").split(". ")[1]
                else:
                    print("Query was not successful. Check your input or try again.")
                    print("Error:", result["queryresult"]["error"])

            elif "go to sleep" in text:
                shutdown_sound()
                break 

            else:
                if count==0:
                    speak = "Sorry, I didn't get that. Can you say it one more time?"                    
                    count+=1
                else:
                    speak = "Sorry, I don't know that, I need to be programmed to understand this. What else can I help you with?"  

        elif boo==False:
            speak = "If you need help with anything, call my name first, then let me know how I can assist you."
                 
        if speak  !=  " ":
            response(speak)

    except:
        response("Something went wrong. Please try again.")
        break
