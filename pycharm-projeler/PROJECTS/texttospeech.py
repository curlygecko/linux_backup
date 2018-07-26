from gtts import gTTS
import urllib3
from bs4 import BeautifulSoup
import requests
import os
urllib3.disable_warnings()
os.chdir("C:\\Users\\dogu2\\Desktop")

url = requests.get("http://www.webtekno.com/steam-de-18-tl-ye-satilan-oyun-kisa-sureligine-ucretsiz-oldu-h49513.html")
content = url.content
soup = BeautifulSoup(content, "html.parser")

metin = soup.find("p")
yazı = metin.getText()
print(yazı)



oku = gTTS(text=yazı, lang="tr")
oku.save("webtekno.mp3")
oku.close()

