# Finding the shortest path in a Wikipedia's graph

Wikipedia is represented by a directed graph structure, where:
- the nodes are articles
- the edges are links.

How the project works:
1. On the site, you can specify the initial and final Wikipedia article
2. The client will send a request to the service with two vertices
3. The service collects Wikipedia articles into the graph structure and traverses it in search of the shortest path between vertices using the transformed Dijkstra's algorithm
4. The service sends the collected data and the shortest path found
5. Then the shortest path between the articles and its length is drawn on the site

### The project is written in python using the following libraries:

- bs4 (BeautifulSoup) - for html page parsing
- django - for project collection (client-server communication, parsing, html page creation)
- requests - for requests
- networkx - for graph construction and calculation of the shortest path
- etc. (less significant)

### The composition of the project:

- testing_wiki.py - Wikipedia parsing file and shortest path calculation. The main function of shortestPath(param1, param2) is to input the beginning and end of the path, in the "string" format.
- buttonpython - setting up client-server interaction


### Launch and connecting to the local network of the host.

**Command to start the server on the local computer:**

- transferring all changes to the database
```
python manage.py migrate
```
- python manage.py runserver 127.0.0.1:5900 //starting a local server

### Launch and connecting to the local network of the host.
- ssh user@remote.host //go to the server
- scp -r /Users/anastasiya_sh/Documents/buttonpython user@remote.host:/some/remote/directory/dir2 //copying directory
- python3 manage.py runserver 0:8000 //launching the project, in setting.py the available host is specified ALLOWED_HOSTS = ['10.55.170.29']
- 'http://10.55.170.29:8000 /' - in the brawser. We log in on a computer connected to a local network. 
