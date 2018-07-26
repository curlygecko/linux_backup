# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

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
        print("\n".join(tr))
        print("******************")
    if decision == "1":
        en_tr()
    elif decision == "2":
        tr_en()

