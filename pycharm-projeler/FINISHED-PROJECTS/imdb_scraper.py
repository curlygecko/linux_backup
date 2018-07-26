from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import os

def top_movies_by_genres():
    genre = input("Genre >> ")
    name = input("Type a name for your excel document: ")
    imdb_page = requests.get("https://www.imdb.com/search/title?genres="+genre.lower()+"&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=9YAKJBBWVSMFF6RYQTAJ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")

    content = imdb_page.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all("h3", class_="lister-item-header")
    ratings = soup.find_all("div", class_="inline-block ratings-imdb-rating")
    directors = soup.find_all(href=re.compile("adv_li_dr"))

    tablo = {"Movie Name":[],
             "Rating":[],
             "Director":[]}

    for title, rating, director in zip(titles, ratings, directors):
        tablo["Movie Name"].append(title.getText())
        tablo["Rating"].append(rating.getText())
        tablo["Director"].append(director.next_element)

    data = pd.DataFrame(tablo)
    writer = pd.ExcelWriter(name + ".xlsx")
    data.to_excel(writer, "sheet")
    writer.close()

    print("THE EXCEL DOCUMENT HAS CREATED SUCCESFULY IN CURRENT DIRECTORY")

def top_rated_tv():
    name = input("Type a name for your excel document: ")
    imdb_page = requests.get("https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=NEV5BK8E1GCPGMHRMF9Q&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_6")

    content = imdb_page.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all("td", class_="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")

    tablo = {"TV Show": [],
             "Rating": []}

    for title, rating in zip(titles, ratings):
        tablo["TV Show"].append(title.getText())
        tablo["Rating"].append(rating.getText())
    data = pd.DataFrame(tablo)
    writer = pd.ExcelWriter(name + ".xlsx")
    data.to_excel(writer, "sheet")
    writer.close()

    print("THE EXCEL DOCUMENT HAS CREATED SUCCESFULY IN CURRENT DIRECTORY")


def top250():
    name = input("Type a name for your excel document: ")
    imdb_page = requests.get("https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=9378VC485FWN7MCWMVR0&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_1")

    content = imdb_page.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all("td", class_="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")

    tablo = {"Movie Name": [],
             "Rating": []}

    for title, rating in zip(titles, ratings):
        tablo["Movie Name"].append(title.getText())
        tablo["Rating"].append(rating.getText())
    data = pd.DataFrame(tablo)
    writer = pd.ExcelWriter(name+".xlsx")
    data.to_excel(writer, "sheet")
    writer.close()

    print("THE EXCEL DOCUMENT HAS CREATED SUCCESFULY IN CURRENT DIRECTORY")

def most_pop():
    name = input("Type a name for your excel document: ")
    imdb_page = requests.get("https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=9378VC485FWN7MCWMVR0&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_1")

    content = imdb_page.content
    soup = BeautifulSoup(content, "html.parser")

    titles = soup.find_all("td", class_="titleColumn")
    ratings = soup.find_all("td", class_="ratingColumn imdbRating")

    tablo = {"Movie Name": [],
             "Rating": []}

    for title, rating in zip(titles, ratings):
        tablo["Movie Name"].append(title.getText())
        tablo["Rating"].append(rating.getText())
    data = pd.DataFrame(tablo)
    writer = pd.ExcelWriter(name+".xlsx")
    data.to_excel(writer, "sheet")
    writer.close()

    print("THE EXCEL DOCUMENT HAS CREATED SUCCESFULY IN CURRENT DIRECTORY")

if not os.path.exists("C:\\Users\\dogu2\\Desktop\\IMDB"):
    os.makedirs("C:\\Users\\dogu2\\Desktop\\IMDB")
os.chdir("C:\\Users\\dogu2\\Desktop\\IMDB")

print("************** IMDB BOT V1.0 ***************")
while True:
    print("What You Want To Scrape ?\nIMDB TOP 250 MOVIES(1)\nMost Popular Movies(2)\nTOP Rated TV Shows(3)\nTOP 250 Movies By Genres(4)\nQUIT(q)")
    decision = input()

    if decision == "1":
        top250()
    elif decision == "2":
        most_pop()
    elif decision == "3":
        top_rated_tv()
    elif decision == "4":
        top_movies_by_genres()
    elif decision == "q" :
        break


