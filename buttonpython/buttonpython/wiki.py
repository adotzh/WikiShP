import networkx as nx
import bs4
import requests
import time
import json
from urllib.parse import quote
import os
import matplotlib.pyplot as plt


#given parameter (url1, url2, header)
def CheckCorrect(url):
    if requests.get(url, headers=header).status_code != 200:
        return "Element not found in wiki"
    else:
        return 1

def PageParser(url):
    r = requests.get(url, headers=header)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    information = soup.find("ul", id="mw-whatlinkshere-list")
    try:
        names = [item.text for item in information.findAll("a")]
        names = [names[3 * i] for i in range(len(names) // 3)]
    except:
        return [], None
    try:
        next_page = domen + soup.find("a", text="следующие 50")["href"]
        return names, next_page
    except:
        return names, None

def ElementParser(WikipediaGraph, element, level):
    element_url = url + quote(str(element.replace(" ", "_")))
    names, next_page = PageParser(element_url)
    GraphLevel = []
    GraphLevel += names
    while next_page is not None:
        names, next_page = PageParser(next_page)
        GraphLevel += names
    GraphCreator(WikipediaGraph, element, GraphLevel)
    #Create file: element_name.json with children's links (children in graph) and children's name
    filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "level_{}.txt".format(level))
    print("\n".join(GraphLevel), file = open(filename, "a"))
    GraphLevel = []
    return filename

def LevelParser(WikipediaGraph, param1, level, elements_file):
    while param1 not in WikipediaGraph:
        with open(elements_file, "r") as leasts:
            for element in leasts:
                if param1 not in WikipediaGraph:
                    element = element.replace("\n", "")
                    elements_file = ElementParser(WikipediaGraph, element, level + 1)
        level += 1
        LevelParser(WikipediaGraph, param1, level, elements_file)
    return level

def GraphCreator(WikipediaGraph, element, names):
    for name in names:
        WikipediaGraph.add_edge(name, element)

def ShortestPath(param1, param2):
    global header 
    global domen 
    global url
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
    domen = "https://ru.wikipedia.org"
    url = domen + "/wiki/"+ "Служебная:Ссылки_сюда" + "/"
    WikipediaGraph = nx.DiGraph()
    WikipediaGraph.clear()
    try:
        url1 = url + quote(str(param1.replace(" ", "_")))
        url2 = url + quote(str(param2.replace(" ", "_")))
    except:
        return "NoneType"
    level = 1
    print(param1, param2)
    if CheckCorrect(url1) != 1 or param1 == "":
        return "First element not found in wiki"
    elif CheckCorrect(url2) != 1 or param2 == "":
        return "Second element not found in wiki"
    else:
        elements_filename = ElementParser(WikipediaGraph, param2, level)
        level = LevelParser(WikipediaGraph, param1, level, elements_filename)
        DrawGraph(WikipediaGraph, param1, param2)
    try:    
        for i in range(level):
            path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "level_{}.txt".format(i + 1))
            os.remove(path)
    except:
        print("Заебок")
    return nx.shortest_path(WikipediaGraph, source=param1, target=param2)


def DrawGraph(WikipediaGraph, param1, param2):
    pos = nx.spring_layout(WikipediaGraph)
    nx.draw(WikipediaGraph, pos, node_color='k', node_size=10)
    #draw path in red
    path = nx.shortest_path(WikipediaGraph, source=param1, target=param2)
    path_edges = set(zip(path,path[1:]))
    labels = dict((path[i], path[i]) for i in range(len(path)))
    nx.draw_networkx_nodes(WikipediaGraph, pos, nodelist=path, node_color='r', node_size=50)
    nx.draw_networkx_labels(WikipediaGraph, pos, nodelist=path, labels=labels, font_color="b",font_size=20, alpha=2.0)
    nx.draw_networkx_edges(WikipediaGraph, pos, edgelist=path_edges, edge_color='r',width=2)
    plt.axis('equal')
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"media/WikipediaGraph.png"))
    plt.clf()

param1 = "Аоки, Кадзуё"
param2 = "Наивность"
ShortestPath(param1, param2)

