import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

page = 1

while True:
    page += 1
    site = requests.get("https://www.ebay.com/sch/Computers-Tablets-Networking-/58058/i.html?_nkw=Asus&_pgn="+str(page))
    content = site.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all("h3", class_="s-item__title")
    prices = soup.find_all("span", class_="s-item__price")
    locations = soup.find_all("span", class_="s-item__location s-item__itemLocation")

    dicto = {"Prices":[],
             "Names":[],
             "Location":[]}

    for price, title,location in zip(prices, titles, locations):
        dicto["Prices"].append(price.getText())
        dicto["Names"].append(title.getText())
        dicto["Location"].append(location.getText())
    brics = pd.DataFrame(dicto)
    print("SAYFA : "+str(page))
    print(brics)

    #with open("pandaebay.txt", "a") as dosya:
        #dosya.write(str(brics))
    brics.to_csv("deneme.csv")
