# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3

class JARVIS:
    def listener(self,recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language="tr-TR")
            return command

    def jarvis(self,command):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty("rate", 130)
        tolga = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga"
        engine.setProperty('voice', tolga)
        engine.say(command)
        engine.runAndWait()
    def david(self,command):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty("rate", 130)
        david = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        engine.setProperty('voice', david)
        engine.say(command)
        engine.runAndWait()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

j = JARVIS()

print("*********Quick Dictionary V1.0*********")
while True:
    print("SELECT\nEN > TR (1)\nTR > EN (2)\nQUIT(q)")
    decision = input()
    if decision == "q":
        break
    print("Kelime/Word >> ")
    wordd = input()
    limit = 0

    url = requests.get("http://tureng.com/en/turkish-english"+"/"+wordd)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    turkceleri = soup.find_all("td", class_="tr ts", lang="tr")
    ingilizceleri = soup.find_all("td", class_="en tm", lang="en")
    
    def en_tr():
        limit = 0
        ing = []
        for kelime in turkceleri:
            limit +=1
            ing.append(kelime.text)
            if limit == 6:
                break
        print("******************")    
        print("\n".join(ing))
        j.jarvis(ing)
        print("******************")
    def tr_en():
        tr = []
        limit = 0
        for kelime1 in ingilizceleri:
            limit +=1
            tr.append(kelime1.text)
            if limit == 6:
                break
        print("******************")
        string = "\n".join(tr)
        for ch in string:
            new_string = string.replace("n.", "")
            new_string = string.replace("v.", "")
            new_string = string.replace("adj.", "")
        print(new_string)
        j.david(new_string)
        print("******************")
    if decision == "1":
        en_tr()
    elif decision == "2":
        tr_en()

