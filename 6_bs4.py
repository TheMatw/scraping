import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

rank1 = soup.find("li", attrs={"class":"rank01"})
ranks = rank1.find_next_siblings("li")
for rank in ranks:
    print(rank.a.get_text())
