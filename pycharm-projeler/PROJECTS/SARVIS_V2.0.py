from bs4 import BeautifulSoup
import requests
import pandas as pd
import speech_recognition as sr
import pyttsx3
import sys
import random

def hava_durumu(city):
    url = requests.get("http://www.hurriyet.com.tr/hava-durumu/"+city+"/")
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    today = soup.find("div", class_="today-weather-r")
    days = soup.find_all("div", class_="weather-box swiper-slide")
    for day in days:
        yazı = day.text
        new_yazı = yazı.replace("ºC", "derece")
        print(new_yazı)
        j.jarvis(new_yazı)

def bugün_hava_durumu(city):
    url = requests.get("http://www.hurriyet.com.tr/hava-durumu/" +city+ "/")
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    today = soup.find("div", class_="today-weather-r")
    days = soup.find_all("div", class_="weather-box swiper-slide")
    bugun = today.getText()
    print(bugun)
    j.jarvis(bugun)

def kapat():
    j.jarvis("görüşmek üzere...")
    print("SARVIS durduruldu")
    sys.exit()

def cevapla():
    cevaplar = "ben çakma bir yapay zekayım", "ben sarvisim", "ben hiçbir şeyim.", "ben salağın tekiyim"
    cevap = random.choice(cevaplar)
    j.jarvis(cevap)
class JARVIS:
    def listener(self,recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source,phrase_time_limit=3)
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

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

j = JARVIS()

def main():
    while True:
        j.jarvis("Dinliyorum")
        print("Dinliyorum")
        try:
            rec = j.listener(recognizer,microphone)
            if "hava durumu" in rec:
                j.jarvis("Hangi şehir ?")
                print("Hangi şehir ?")
                city = j.listener(recognizer,microphone)
                hava_durumu(city)
            elif "bugün hava" in rec:
                j.jarvis("Hangi şehir ?")
                print("Hangi şehir ?")
                city = j.listener(recognizer, microphone)
                bugün_hava_durumu(city)
            elif "kapat" in rec:
                kapat()
            elif "sen nesin" or "sen" or "nesin" in rec:
                cevapla()


        except sr.UnknownValueError:
            j.jarvis("Anlayamadım.Tekrar söyler misin ?")

main()
