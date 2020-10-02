# Client-Server
Wikipedia shortest path between two object

Команда для запуска сервера на локальном компьютере: 
- перенос всех изменений в базу данных
```
python manage.py migrate
```
- python manage.py runserver 127.0.0.1:5900 //запуск локального сервера

Проект написан на языке python c использованием следующих библиотек:
- bs4 (BeautifulSoup) - для парсинга html страниц
- django - для сбора проекта (общение клиент-сервер, парсинг, создание html - страницы)
- requests - для запросов
- networkx - для построение графа и рассчета кратчайшего пути
- и др. (менее значимые)

Состав проекта:
- wiki.py - файл парсинга Википедии и рассчета кратчайшего пути. Основная функция ShortestPath(param1, param2) - на вход начало и конце пути, формата "string".
- 
-



Подключение в локальной сети host'инга:

Вариант1
- ssh user@remote.host //заходим на сервер
- scp -r  /Users/anastasiya_sh/Documents/buttonpython user@remote.host:/some/remote/directory/dir2 //копируем дирректорию
- python3 manage.py runserver 0:8000 //запускаем проект, в setting.py указан доступный хост ALLOWED_HOSTS = ['10.55.170.29']
- заходим на компьютере, подключенном к локальной сети в браузере 'http://10.55.170.29:8000/'


