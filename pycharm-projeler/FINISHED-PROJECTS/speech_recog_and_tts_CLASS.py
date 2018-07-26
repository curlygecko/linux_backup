import speech_recognition as sr
import urllib3
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pyttsx3
import webbrowser


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

j = JARVIS()


print("Listening...")
try:
    rec = j.listener(recognizer,microphone)
    if "Google" in rec:
        j.jarvis("google açılıyor")
        webbrowser.open_new_tab("https://www.google.com/")
    elif "toplama" in rec:
        j.jarvis("İlk sayıyı söyle: ")
        topla_1 = j.listener(recognizer,microphone)
        j.jarvis("İkinci sayıyı söyle: ")
        topla_2 = j.listener(recognizer,microphone)
        toplam = str((int(topla_1)+int(topla_2)))
        j.jarvis("Toplam eşittir "+toplam)

except sr.UnknownValueError:
    print("say again")
