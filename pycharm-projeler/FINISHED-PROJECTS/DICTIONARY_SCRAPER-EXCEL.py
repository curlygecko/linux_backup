import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd
import xlsxwriter
import os
import shutil

os.mkdir("C:\\Users\\dogu2\\Desktop\\tureng\\")
os.chdir("C:\\Users\\dogu2\\Desktop\\tureng\\")
dire = os.getcwd()
shutil.copy("C:\\Users\\dogu2\\Desktop\\pycharm-projeler\\PROJECTS\\chromedriver.exe", dire)


print("*********CURDEV DICTIONARY SCRAPER V1.0*********")
tur = 0
words = []
while len(words) < 5:
    word = input("Word: ")
    words.append(word)
print(words)
for i in words:
    driver = webdriver.Chrome()
    driver.get("http://tureng.com/en/english-turkish")
    kutu = driver.find_element_by_tag_name("input")
    kutu.send_keys(i)
    kutu.send_keys(Keys.ENTER)

    url = requests.get("http://tureng.com/en/turkish-english"+"/"+i)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")


    turkceleri = soup.find_all("td", class_="tr ts")
    ingilizceleri = soup.find_all("td", class_="en tm")

    tablo = {"English":[],
            "Turkish":[]}

    for ingilizce, turkcesi in zip(ingilizceleri, turkceleri):
        tablo["English"].append(ingilizce.getText())
        tablo["Turkish"].append(turkcesi.getText())

    data = pd.DataFrame(tablo)
    print(data)

    for word_count in words:
        writer = pd.ExcelWriter(i+".xlsx")
        data.to_excel(writer, "sheet")
        writer.close()
