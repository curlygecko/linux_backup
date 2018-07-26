from bs4 import BeautifulSoup
import requests
import pandas as pd
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

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

j = JARVIS()

j.jarvis("Şehir ismini söyle")
city = j.listener(recognizer, microphone)

url = requests.get("https://www.ntvhava.com/konum/eskisehir/3-gunluk-hava-tahmini")
content =url.content
soup = BeautifulSoup(content, "html.parser")

günler = soup.find_all("div", class_="date")
sıcaklıklar = soup.find_all("span", class_="range1 font25")
durumlar = soup.find_all("p", class_="font18 range1")


tablo = {"Sıcaklık":[],
         "----Gün-----":[],
         "-------Durum-------": []}

for gün,sıcaklık, durum in zip(günler,sıcaklıklar, durumlar):
    tablo["-------Durum-------"].append(durum.getText())
    tablo["----Gün-----"].append(gün.getText())
    tablo["Sıcaklık"].append(sıcaklık.getText())

data = pd.DataFrame(tablo)

data = data.astype(str)

print(data)
j.jarvis(data)
