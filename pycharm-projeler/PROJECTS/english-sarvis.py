import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty("rate", 130)
zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', zira)
engine.say("hello my friends")
engine.runAndWait()