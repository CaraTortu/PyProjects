import pyautogui as pyg
import webbrowser as wb
import os, sys, json, re, webbrowser, click
import time as tm
from datetime import *
from requests import Request, Session, get, post, Session
from urlextract import URLExtract
import speech_recognition as sr
from playsound import playsound

whatsaid = ''
len = ''
canihear = True

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

def join_meeting_jitsi(url, toLeave):

    webbrowser.open(url, new=1)

    #####################################
    # LOGIN

    tm.sleep(3)  
    for i in range(0,3):
        pyg.click(892, 268)
    pyg.write('javier.diaz42')
    for i in range(0,3):
        pyg.click(884, 309)
    pyg.write('') #password
    pyg.click(1106, 371)
    
    #####################################
    # MUTE MIC

    tm.sleep(3)
    pyg.click(893, 1034)

    #####################################
    # CLOSE CALL IF ITS TIME

    playsound("holaatodos.wav")

    conditionss = open("conditions.json" , 'r')
    conditions = json.loads(conditionss.read())

    while True:
        time.sleep(0.5)
        x = datetime.now()
        if toLeave == str(x.strftime("%H-%M-%S")):
            pyg.click(962, 1036)
            tm.sleep(2)
            pyg.click(232, 43)
            break
        else:
            pass

        whatsaid = mic_hear(2, len)
        for condition in conditions:
            if condition in whatsaid:
                pyg.keydown('space')
                playsound(conditions[str(condition)])
                pyg.keyUp('space') 
    
def join_meeting_jitsi_password(url, toLeave, passwd):


    webbrowser.open(url, new=1)

    #####################################
    # LOGIN

    tm.sleep(3)  
    for i in range(0,3):
        pyg.click(892, 268)
    pyg.write('javier.diaz42')
    for i in range(0,3):
        pyg.click(884, 309)
    pyg.write('p2-8f6TJ')
    pyg.click(1106, 371)
    

    #####################################
    # MUTE MIC

    tm.sleep(3)
    pyg.click(893, 1034)

    #####################################
    # CLOSE CALL IF ITS TIME
    pyg.keydown('space')
    playsound("holaatodos.wav")
    pyg.keyUp('space')

    conditionss = open("conditions.json" , 'r')
    conditions = json.loads(conditionss.read())

    while True:
        x = datetime.now()
        if toLeave == str(x.strftime("%H-%M-%S")):
            pyg.click(962, 1036)
            tm.sleep(2)
            pyg.click(232, 43)
            break
        else:
            pass

        whatsaid = mic_hear(2)
        for condition in conditions:
            if condition in whatsaid:
                pyg.keydown('space')
                playsound(conditions[str(condition)])
                pyg.keyUp('space')

def join_meeting_webex(url, toLeave, len):

    webbrowser.open(url, new=1)
    tm.sleep(2)
    pyg.click(758, 435)

    #####################################
    # START CAUSE EVERYTHING IS MUTED

    tm.sleep(8)
    pyg.click(1168, 1038)

    #####################################
    # CLOSE CALL IF ITS TIME

    tm.sleep(10)

    if len == 'es':
        pyg.click(725,1047)
        tm.sleep(0.5)
        playsound("holaatodos.wav")
        tm.sleep(0.5)
        pyg.click(725,1047)
    elif len == 'en':
        pyg.click(725,1047)
        tm.sleep(0.5)
        playsound("hellothere.wav")
        tm.sleep(0.5)
        pyg.click(725,1047)

    conditionss = open("conditions.json" , 'r')
    conditions = json.loads(conditionss.read())

    while True:
        tm.sleep(0.3)
        x = datetime.now()
        if toLeave == str(x.strftime("%H-%M-%S")):
            pyg.click(1240, 942)
            tm.sleep(0.5)
            pyg.click(1084, 608)
            tm.sleep(0.5)
            pyg.click(229, 46)
            break

        global whatsaid

        if whatsaid != None:
            print(whatsaid)
        for condition in conditions:
            if str(condition) in str(whatsaid):
                pyg.click(725,1047)
                tm.sleep(0.5)
                playsound(conditions[str(condition)])
                tm.sleep(0.5)
                pyg.click(725,1047)
            if "bye" in str(whatsaid) or "goodbye" in str(whatsaid) or "see you" in str(whatsaid):
                pyg.click(1818,1053)
                tm.sleep(0.5)
                pyg.click(1613, 962)
                pyg.write("See y'all other day")
                tm.sleep(1)
                pyg.click(1240, 942)
                tm.sleep(0.5)
                pyg.click(1084, 608)
                tm.sleep(0.5)
                pyg.click(229, 46)
                break
    get_calls()

def get_url(url):

    with open("urls.json", 'r+') as urlss:
        urls_text = json.loads(urlss.read())

        if url in urls_text:
            return urls_text[str(url)]
        elif url not in urls_text:
            urll = str(url) + "&action=joinmeeting"
            urls_text[url] = urll
            urlss.seek(0)
            urlss.truncate()
            json.dump(urls_text, urlss, indent=4)
            return urll

def get_calls():
    x = datetime.now() # Get time
    year, month, day = str(date.today()).split('-') # Get todays year, month and day
    hour, minute, second = str(x.strftime("%H-%M-%S")).split('-') # Get nows hour, minute and second

    ###########################################################################################################
    # Setup the schedule

    filee = open('schedule.json', 'r') # Open schedule.txt
    schedule = json.loads(filee.read()) # Read the file
    filee.close() # Close the file

    classes = schedule["classes"]
    global len
    global canihear

    ###########################################################################################################
    # START
    while True:
        tm.sleep(0.1)
        for c in classes:
            x = datetime.now() # Get time
            full_time = str(x.strftime("%H-%M-%S"))

            typee = schedule["classes"][str(c)]["type"]
            urrl = get_url(str(schedule["classes"][str(c)]["url"]))
            len = str(schedule["classes"][str(c)]["len"])

            if canihear == True:
                mic_hear(3, len)
                canihear = False

            if str(schedule["classes"][str(c)]["start"]) == full_time and urrl != '':
                try:
                    if schedule["classes"][str(c)]["password"]:
                        join_meeting_jitsi_password(str(urrl), str(schedule["classes"][str(c)]["finish"]), str(schedule["classes"][str(c)]["password"]))
                except KeyError:
                    if typee == 'jitsi':
                        join_meeting_jitsi(str(urrl), str(schedule["classes"][str(c)]["finish"]))
                    elif typee == 'webex':
                        join_meeting_webex(str(urrl), str(schedule["classes"][str(c)]["finish"]), len)
            else:
                pass

get_calls()
