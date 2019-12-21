import bs4
import re
import requests
import datetime
import time


region = {'Москва': 4368,
'Санкт-Петербург': 4079,
'Новосибирск': 4690,
'Екатеринбург': 4517,
'Нижний Новгород': 4355,
'Казань': 4364,
'Челябинск': 4565,
'Омск': 4578,
'Самара': 4618,
'Ростов-на-Дону': 5110,
'Уфа': 4588,
'Красноярск': 4674,
'Воронеж': 5026,
'Пермь': 4476,
'Волгоград': 5089}


def correct(date, city):
    try:
        time.strptime(date, '%Y.%m.%d')
        if city not in region:
            return 'Invalid city!'
        else:
            return 1
    except ValueError:
        return 'Invalid date!'

def parse(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
    try:
        r = requests.get(url, headers=header)
    except Exception as e:
        print("ERROR with connection to the site")
    if r.status_code == 200:
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        table = soup.find("table", {"align":"center"})
        line = soup.find("table", {"align": "center"}).find('tbody').find_all('tr')
        data = []
        for row in line:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        print (data)
        return data

def AVG(date, city):
    year, month, day = date.split(".")
    if correct(date, city) != 1:
        return correct(date, city)
    param = [0, 0, 0]
    if int(year + month + day) > int(datetime.date.today().strftime("%Y%m%d")) - 2:
        year = 2018
        day = int(day)
        for i in range(10):
            url = "https://www.gismeteo.ru/diary/" + str(region[city]) + "/" + str(year - i) + "/" + month
            data = parse(url)
            param[0] += ((int(data[day - 1][1]) + int(data[day - 1][4]))/2)
            param[1] += ((int(data[day - 1][2]) + int(data[day - 1][5]))/2)
            param[2] += ((int(data[day - 1][3].split()[1][:-3]) + int(data[day - 1][6].split()[1][:-3]))/2)
        return [par/10 for par in param]
    else:
        url = "https://www.gismeteo.ru/diary/" + str(region[city]) + "/" + str(year) + "/" + month
        data = parse(url)
        day, year = int(day), int(year)
        param[0] = (int(data[day - 1][1]) + int(data[day - 1][4]))/2
        param[1] = (int(data[day - 1][2]) + int(data[day - 1][5]))/2
        param[2] = (int(data[day - 1][3].split()[1][:-3]) + int(data[day - 1][6].split()[1][:-3]))/2
        return param


date = '2019.10.31'
city = 'Москва'
print(AVG(date, city))
