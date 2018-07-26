# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("*********Quick Dictionary V1.0*********")
while True:
    print("SELECT\nEN > TR (1)\nTR > EN (2)\nQUIT(q)")
    decision = input()
    if decision == "q":
        break
    elif decision == "1":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Kelime/Word söyle >> ")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=5)
        kelime = r.recognize_google(audio, key=None, language="en-US")
        print("Aranan kelime : "+kelime)
    elif decision == "2":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Kelime/Word söyle >> ")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=5)
        kelime = r.recognize_google(audio, key=None, language="tr-TR")
        print("Aranan kelime : "+kelime)
    limit = 0

    url = requests.get("http://tureng.com/en/turkish-english" + "/" + kelime)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    turkceleri = soup.find_all("td", class_="tr ts", lang="tr")
    ingilizceleri = soup.find_all("td", class_="en tm", lang="en")


    def en_tr():
        limit = 0
        ing = []
        for kelime in turkceleri:
            limit += 1
            ing.append(kelime.text)
            if limit == 6:
                break
        print("******************")
        print("\n".join(ing))
        print("******************")


    def tr_en():
        tr = []
        limit = 0
        for kelime1 in ingilizceleri:
            limit += 1
            tr.append(kelime1.text)
            if limit == 6:
                break
        print("******************")
        print("\n".join(tr))
        print("******************")


    if decision == "1":
        en_tr()
    elif decision == "2":
        tr_en()

