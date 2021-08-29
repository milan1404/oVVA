from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from Database import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
#from PySide2.QtUiTools import loadUiType
import scifi
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
# import database
import pyttsx3
from PIL import ImageGrab
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import random
import os
import speech_recognition as sr
from time import sleep
from selenium import webdriver
import wikipedia
from time import strftime
import time, sys
import subprocess
import pyautogui
import requests
from tkinter import *
import psutil
import requests, json
import wolframalpha

# from lsHotword import ls


try:
    app = wolframalpha.Client("6JJ3Q4-7KJR3Q7U7L")
except Exception:
    print("unstable connection")

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

info = ['I am oliVIA, a simple but efficient virtual assistant made by a MILAN',
        'I am your father,rofl', 'I am oliVIA,I said that a ton of times already',
        'I am the one who needs no gun to get respect from no one on the street']
booting_startup = ['oliVIA Assistant version 1.0 has begun', 'oliVIA at your service',
                   'Currently starting oliVIA Virtual Assistant', "Loading drivers and modules",
                   "oliVIA assistant is booting up"]
greet = ["hello", "hello there", "Hi,I am oliVIA", "What is up user", "oliVIA at your service",
         "Greetings organic lifeform", "how can I help you today", "Greetings human", "Your wish is my command",
         "Hello user", "Hello user,what would you like to do"]  # Possible responses to user greetings
userGreet = ["how can I be of assistance today", "your wish is my command",
             "I am oliVIA,your personal virtual assistant", "how are you today"]
closing = ['Shutting down', 'Closing oliVIA Assistant', 'Have a nice day'
                                                        'khatam,tata ,byebye', ]
feelings = ["I have no feelings,I am not sentient like you probably are", "I am feeling like a million bytes",
            "I am feeling functional and ready to serve"]
musical = ["What are we watching today", "Are gonna to sing some karaoke", "Listening to some music today",
           "Good thing I have my dancing module inside me", "My favorite youtuber is MILAN",
           "Let's start our own channel,whatsay"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")


def collect_info():
    engine.say(random.choice(booting_startup))
    engine.runAndWait()
    engine.say("enter YOUR sweet NAME please")
    engine.runAndWait()
    name = input("Your name:")
    engine.say("enter YOUR MAIL-ID")
    engine.runAndWait()
    Mail_id = input("Your mail-id:")
    engine.say("enter YOUR current location")
    engine.runAndWait()
    location = input("Your current location:")

    #sqlFormula = "INSERT INTO USER_DETAILS (NAME,MAIL_ID,LOCATION) VALUES (%s, %s, %s)"
    #info1 = [name, Mail_id, location]
    #mycursor.execute(sqlFormula, info1)
    #mydb.commit()







def execution():
    sqlFormula=("INSERT INTO user_details (NAME, MAIL-ID, LOCATION) VALUES (%s, %s, %s)")
    info1=[(name,Mail_id,location)]
    mycursor.execute(sqlFormula,info1)
    mydb.commit()

















class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.OLIVIA()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recognising......")
            text = R.recognize_google(audio, language='en-in')
            print(">> ", text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def OLIVIA(self):
        wish()
        #collect_info()
        #speak("Hello " + name + random.choice(userGreet))


        while True:

            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            if 'king of the jungle' in self.query:
                speak("Milan also called as the indian lion is also called the king of the jungle. ")
            if 'hello' in self.query:
                speak(random.choice(greet))
                #for hai
            if 'how are you' in self.query:
                speak(random.choice(feelings))
                #for feels
            if 'open google' in self.query:
                webbrowser.open('www.google.co.in')
                speak("opening google")
            if 'open youtube' in self.query:
                speak(random.choice(musical))
                speak("opening youtube")
                webbrowser.open("www.youtube.com")
            if 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir = "./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir, self.musics[0]))
            if 'calculate' in self.query:
                def add(num1, num2):
                    return num1 + num2
                def subtract(num1, num2):
                    return num1 - num2
                def multiply(num1, num2):
                    return num1 * num2
                def divide(num1, num2):
                    return num1 / num2

                print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n")
                select = int(input("Select operations form 1, 2, 3, 4 :"))

                number_1 = int(input("Enter first number: "))
                number_2 = int(input("Enter second number: "))

                if select == 1:
                    print(number_1, "+", number_2, "=",
                          add(number_1, number_2))
                elif select == 2:
                    print(number_1, "-", number_2, "=",
                          subtract(number_1, number_2))
                elif select == 3:
                    print(number_1, "*", number_2, "=",
                          multiply(number_1, number_2))
                elif select == 4:
                    print(number_1, "/", number_2, "=",
                          divide(number_1, number_2))
                else:
                    print("Invalid input")
            if 'search' in self.query:
                speak("Opening web browser to search for " + self.query.split("search", 1)[1])

                webbrowser.open_new_tab("http://google.com/search?q=" + self.query.split("search", 1)[1])
                # driver = webdriver.Chrome()
                # driver.get("http://google.com/search?q=" + data.split("search", 1)[1])
                wordSearch = self.query.split("search", 1)[1]
                sentence = wikipedia.summary(wordSearch, sentences=2)
                engine.say(sentence)
                engine.runAndWait()
            if 'time' in self.query:
                current = strftime("%I:%M")
                speak("The current time is " + current)
            if 'date' in self.query:
                dateT = strftime("%B:%d:%A:%Y")
                speak("Today's date is " + dateT)
            if 'make a joke' in self.query:
                speak("playing a random joke")
                joke1 = ("Hear about the new restaurant called Karma, There’s no menu,  You get what you deserve.")
                speak(joke1)
            if 'mail' in self.query:
                speak("Opening Email Client")
                Call_URL = "http://gmail.com"
                mycmd = r'start chrome /new-tab {}'.format(Call_URL)
                subprocess.Popen(mycmd, shell=True)
            if 'Amazon' in self.query:                #not working ...check later on
                speak("Opening Amazon to purchase ")
                mycmd = r'start chrome /new-tab {}'.format(Call_URL)
                subprocess.Popen(mycmd, shell=True)
            if 'screenshot' in self.query:
                speak("Taking screenshot")
                name1 = random.randint(1000, 300000)
                ImageGrab.grab().save("screenshot" + str(name1), "JPEG")
                speak("Screenshot saved as " + name1)
            if 'who am I' in self.query:
                engine.say("You are " + name)
                #says user name
            if 'change voice' in self.query:
                engine.setProperty('voice', voices[random.randrange(0, 2)].id)
                speak("Voice now changed,if not use command again")
            if 'notepad' in self.query:
                speak("Opening notepad")
                subprocess.Popen('notepad.exe')
            if 'shut down' in self.query:
                speak(random.choice(closing))
                sys.exit()
            if 'thank you' in self.query:
                speak("You are welcome")
                #for closing
            if 'olivia' in self.query:
                speak("Yes, I am here")
                #says her name















FROM_MAIN, _ = loadUiType(os.path.join(os.path.dirname(__file__), "./scifi.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920, 1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")
        # self.m = collect_info()

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 8)))

    # self.label_3.setText("<font size=15 color='white'>"+self.m+"</font>")
    # self.label_3.setFont(QFont(QFont('Acens',15)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())