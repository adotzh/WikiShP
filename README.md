# Client-Server
Wikipedia shortest path between two object

Команда для запуска сервила на локальном компьютере: 
- python manage.py migrate //перенос всех изменений в базу данных
- python manage.py runserver 127.0.0.1:5900 //

Проект написан на языке python c использованием следующих библиотек:
- bs4 (BeautifulSoup) - для парсинга html страниц
- django - для сбора проекта (общение клиент-сервер, парсинг, создание html - страницы)
- 


Подключение в локальной сети host'инга:

Вариант1
- ssh user@remote.host //заходим на сервер
- scp -r  /Users/anastasiya_sh/Documents/buttonpython user@remote.host:/some/remote/directory/dir2 //копируем дирректорию

Вариант2
- добавляем в settings.py сточку ALLOWED_HOSTS=[///]
- запускаем командой python manage.py runserver  0.0.0.0:8000


