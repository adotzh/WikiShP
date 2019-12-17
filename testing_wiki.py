import networkx as nx
import bs4
import re
import requests
import datetime
import time
import json
from urllib.parse import quote


#given parameter (url1, url2, header)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
domen = "https://ru.wikipedia.org"
url = domen + "/wiki/"+ "Служебная:Ссылки_сюда" + "/"

def CheckCorrect(url1, url2):
    if requests.get(url1, headers=header).status_code != 200:
        return "First element not found in wiki"
    elif requests.get(url2, headers=header).status_code != 200:
        return "Second element not found in wiki"
    else:
        return 1


WikipediaGraph = nx.DiGraph()

param1 = "Туризм"
param2 = "Туризм"
def PageParser(url):
    r = requests.get(url, headers=header)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    information = soup.find("ul", id="mw-whatlinkshere-list")
    links = [domen + str(item["href"]) for item in information.findAll("a")]
    links = [links[3 * i + 1] for i in range(len(links) // 3)]
    names = [item.text for item in information.findAll("a")]
    names = [names[3 * i] for i in range(len(names) // 3)]
    try:
        next_page = domen + soup.find("a", text="следующие 50")["href"]
        return links, names, next_page
    except:
        return links, names, None

def GraphCreator(Element, names):
    for name in names:
        WikipediaGraph.add_edge(Element,name)

def ShortestPath(param1, param2):
    url1 = url + str(param1.replace(" ", "_"))
    url2 = url + str(param2.replace(" ", "_"))
    if CheckCorrect(url1, url2) != 1:
        return CheckCorrect(url1, url2)
    else:
        links, names, next_page = PageParser(url2)
        print(links, names, file=open("links.html", "a"))
        while next_page is not None:
            print(next_page)
            links, names, next_page = PageParser(next_page)
            print(links, names, file=open("links.html", "a"))
        return links

ShortestPath(param1, param2)


WikipediaGraph = nx.DiGraph()
WikipediaGraph.add_edge(1,2)