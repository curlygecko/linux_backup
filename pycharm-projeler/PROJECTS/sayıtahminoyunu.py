import speech_recognition as sr
import pyttsx3
import random


class JARVIS:
    def listener(self, recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, phrase_time_limit=3)
            command = recognizer.recognize_google(audio, language="tr-TR")
            return command

    def jarvis(self, command):
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


def sayı_tut():

        sayı = random.randint(0, 10)
        sayı_str = str(sayı)
        tutulan = sayı_str
        limit = 0


        while True:
            print("TAHMİN OYUNU")
            print("Tuttuğum sayıyı 3 denemede bilmen gerekiyor")
            j.jarvis("Tuttuğum sayıyı 3 denemede bilmen gerekiyor")

            j.jarvis("Tuttum, tahminini söyle")
            try:
                print("Tahmin et")
                rec = j.listener(recognizer, microphone)
                if rec == tutulan:
                    print("Tebrikler! Bildin")
                    j.jarvis("Tebrikler! Bildin")
                    break
                else:
                    print("Bilemedin.Tekrar dene")
                    j.jarvis("Bilemedin.Tekrar dene")
                    continue

                    limit += 1
                    if limit == 3:
                        print("Hakkın doldu.Tuttuğum sayı "+tutulan)
                        j.jarvis("Tahmin hakkın doldu.Tuttuğum sayı "+tutulan)
                        break
                        print("Tekrar oynamak ister misin ?")
                        j.jarvis("Tekrar oynamak ister misin ?")
                        j.listener(recognizer,microphone)
                        if rec == "evet":
                            continue
                        else:
                            break
            except sr.UnknownValueError:
                print("Tahminin anlaşılmadı, tekrar söyle")
                j.jarvis("Tahminin anlaşılmadı, tekrar söyle")


sayı_tut()


