import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/series/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    series = []
    for item in items:
        series.append({
            "title": item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            "desc": item.find('div', class_="b-content__inline_item-link").find('div').getText(),
            "link": item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            "image": item.find('div', class_="b-content__inline_item-cover").find('a').find('img').get('src'),
        })

    return series
    #print(series)

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        series = []
        for page in range(1, 2):
            # print(f"{URL}page/{page}/")
            html = get_html(f"{URL}/page/{page}/")
            series.extend(get_data(html.text))
        return series
    else:
        raise Exception('Error in parser!!!')


