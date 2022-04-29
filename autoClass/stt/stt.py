import speech_recognition as sr
from playsound import playsound
import pyautogui as pyg
import time as tm
import os
from threading import Thread

timee = 2
len = "en"
whatsaid = ''

def callback(recognizerr, audioo):
    global whatsaid
    global len
    try:
        whatsaid = recognizerr.recognize_google(audioo, language=len)
    except sr.UnknownValueError:
        whatsaid = "IDK"

def mic_hear(timee, len):
    global whatsaid
    r = sr.Recognizer()
    m = sr.Microphone()

    audio = r.listen_in_background(m, callback, phrase_time_limit=timee)


mic_hear(timee, len)

while True:
    if whatsaid != None and whatsaid != '': 
        print(whatsaid)
        whatsaid = ""
