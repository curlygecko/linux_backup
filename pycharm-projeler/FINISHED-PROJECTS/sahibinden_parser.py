import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser


def sahibinden():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = requests.get("https://www.sahibinden.com/kiralik-daire/antalya-kepez-ahatli-kultur-mah.?a103713=true&pagingSize=50&a20=38470",headers=headers)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    ilanlar = soup.find_all("a", class_="classifiedTitle")
    fiyatlar = soup.find_all("td", class_="searchResultsPriceValue")

    for ilan in ilanlar:
        linkler = soup.find_all("a", class_="classifiedTitle")

    print("2+1 KÜLTÜR EŞYALI KİRALİK DAİRE SONUÇLARI: ")

    for ilan,fiyat,link in zip(ilanlar,fiyatlar,linkler):
        ilan_link = "https://www.sahibinden.com"+link.get("href")
        print("-----------------------------------------------------------------------------------------")
        print(ilan.getText()+fiyat.getText())
        print(ilan_link)
       
sahibinden()




