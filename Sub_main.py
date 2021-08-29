#import database
import pyttsx3
from PIL import ImageGrab
import webbrowser
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import random
import os
import speech_recognition as sr
from time import sleep
from selenium import webdriver
import wikipedia
from time import strftime
import time, sys
import datetime
import subprocess
import pyautogui
import requests
from tkinter import *
import psutil
import requests, json


#db connection
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="milan",               #password for user
  database="OLIVIA_DB",               #database name
    auth_plugin = 'mysql_native_password',

)
mycursor=mydb.cursor()
#db connection
from PySide2.QtUiTools import loadUiType


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)
r = sr.Recognizer()


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
           'khatam,tata ,byebye',]
feelings = ["I have no feelings,I am not sentient like you probably are", "I am feeling like a million bytes",
            "I am feeling functional and ready to serve"]
musical = ["What are we watching today", "Are gonna to sing some karaoke", "Listening to some music today",
           "Good thing I have my dancing module inside me", "My favorite youtuber is MILAN",
           "Let's start our own channel,whatsay"]

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        engine.say("Good morning")
    elif hour>=12 and hour<18:
        engine.say("Good Afternoon")
    else:
        engine.say("Good EVENING")

#detail_start
engine.say(wish())
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
sqlFormula="INSERT INTO USER_DETAILS (NAME,MAIL_ID,LOCATION) VALUES (%s, %s, %s)"
info1=[name,Mail_id,location]
mycursor.execute(sqlFormula,info1)
mydb.commit()
#details_stop

engine.say("Hello " + name + random.choice(userGreet))
engine.runAndWait()


def greet(data):
    engine.say(random.choice(greet))
    engine.runAndWait()
    main()
def makeJoke():
    engine.runAndWait()
    joke1=("wanna hear a joke,nikal lavde")
    engine.say(joke1)
    engine.runAndWait()
    main()
def search(data):
    webbrowser.open_new_tab("http://google.com/search?q=" + data.split("search", 1)[1])
   # driver = webdriver.Chrome()
   # driver.get("http://google.com/search?q=" + data.split("search", 1)[1])
    wordSearch = data.split("search", 1)[1]
    sentence = wikipedia.summary(wordSearch, sentences=2)
    engine.say(sentence)
    engine.runAndWait()
    main()
def youtube(data):
    engine.say(random.choice(musical))
    engine.runAndWait()
    Call_URL = "http://youtube.com"
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd, shell=True)
    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

    sleep(2)
    main()
def time(data):
    current = strftime("%I:%M")
    engine.say("The current time is " + current)
    engine.runAndWait()
    main()
def tDate(date):
    dateT = strftime("%B:%d:%A:%Y")
    engine.say("Today's date is " + dateT)
    engine.runAndWait()
    main()
def Gmail(data):
    engine.say("Opening Email Client")
    engine.runAndWait()
    Call_URL = "http://gmail.com"
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd, shell=True)
    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://gmail.com")
    main()
def Amazon(data):
    engine.say("Opening Amazon to purchase " + data.split('buy', 1)[1])
    engine.runAndWait
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(
        "https://www.amazon.com/s/field-keywords=", data.split('buy', 1)[1])
    main()
def Screenshot1():
    engine.say("Taking screenshot")
    engine.runAndWait()
    name = random.randint(1000, 300000)
    time.sleep(5)
    ImageGrab.grab().save("screenshot" + str(name), "JPEG")
    engine.say("Screenshot saved at " + name)
    engine.runAndWait()
    print("Screenshot saved at" + name)
    main()
def calculate(data):
    if 'plus' in data:
        str.replace("plus", "+")

    value1, value2 = (data.split('calculate', 1)[1])
    answer = value1 + value2
    engine.say("The answer to that is " + answer)
    engine.runAndWait()
def calculator():
    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1, num2):
        return num1 / num2
    print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n")

    # Take input from the user
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
def locate(data):
    place = data.split('locate', 1)[1]
    engine.say("Locating " + place)
    engine.runAndWait()
    Call_URL = place
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd, shell=True)
    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.ca/maps/place/"+place+"/")
    main()
def goto(data):
    where = data.split('go to', 1)[1]
    Call_URL = where
    engine.say("Navigating to" + where)
    engine.runAndWait()
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd, shell=True)
    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://"+where.strip())

    main()
def main():
    with sr.Microphone() as source:
        sleep(1)
        print("Say something............")
        audio = r.listen(source)
        sleep(1)
        #print("\n" * 50)

    try:
        data = r.recognize_google(audio)
        print("You voice sounded me like:" + data)
        if data == 'hello':
            greet()

        elif 'search' in data:
            engine.say("Opening web browser to search for " + data.split("search", 1)[1])
            engine.runAndWait()
            search(data)
        elif 'YouTube' in data:
            youtube(data)
        elif 'time' in data:
            time(data)
        elif 'date' in data:
            tDate(data)
        elif data == 'shutdown':
            engine.say(random.choice(closing))
            #engine.runAndWait()    #system halts for more time if prompted
            sys.exit()
        elif 'thank you' in data:
            engine.say("You are welcome")
            #engine.runAndWait()  #system halts for more time if prompted
        elif data == 'oliVIA':
            engine.say("Yes, I am here")
        elif data == 'email':
            Gmail(data)
        elif 'buy' in data:
            print("I recommend u to use Amazon")
            Amazon(data)
        elif data == 'screenshot':
            Screenshot1()
        elif 'calculator' in data:
            calculator()
        elif 'locate' in data:
            locate(data)
        elif data == 'Notepad':
            engine.say("Opening notepad")
            engine.runAndWait()
            subprocess.Popen('notepad.exe')

            main()
        elif data == 'change voice':
            engine.setProperty('voice', voices[random.randrange(0, 2)].id)
            engine.say("Voice now changed,if not use command again")
            engine.runAndWait()
            main()
        elif data == 'tell me a joke':
            makeJoke()
        elif 'go to' in data:
            goto(data)
        elif 'type' in data:
            text = data.split('type', 1)[1]

            pyautogui.typewrite(text)
            main()
        elif data == 'who am I':
            engine.say("You are " + name)
            engine.runAndWait()
            main()
        elif data== 'what is my email':
            engine.say("your email is "+ Mail_id)
            engine.runAndWait()
            main()
        elif data == 'who are you':
            engine.say(random.choice(info))
            engine.runAndWait()
            main()
        elif data == 'how are you':
            engine.say(random.choice(feelings))
            engine.runAndWait()
            main()

        else:
            main()



    except sr.UnknownValueError:
        sleep(2)
        engine.say("MILAN didnot create me to waste time, so please do say something...")
        engine.runAndWait()
        main()
    except sr.RequestError as e:
        print("Could not request results from internet;{0}".format(e))
        main()


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
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

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())

main()