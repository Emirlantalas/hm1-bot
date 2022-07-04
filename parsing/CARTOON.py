import requests
from bs4 import BeautifulSoup


URL_carton = "https://rezka.ag/cartoons/"

HEADERS_2 = {
    "Accept": "ext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.3"

}

def get_html_2(url, params=''):
    req = requests.get(url, headers=HEADERS_2, params=params)
    return req

def get_data_2(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    cartoon = []
    for item in items:
        cartoon.append({
            "title": item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            "desc": item.find('div', class_="b-content__inline_item-link").find('div').getText(),
            "link": item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            "image": item.find('div', class_="b-content__inline_item-cover").find('a').find('img').get('src'),
        })

    return cartoon
    #print(series)

def parser_2():
    html = get_html_2(URL_carton)
    if html.status_code == 200:
        cartoon = []
        for page in range(1, 2):
            # print(f"{URL}page/{page}/")
            html = get_html_2(f"{URL_carton}/page/{page}/")
            cartoon.extend(get_data_2(html.text))
        return cartoon
    else:
        raise Exception('Error in parser!!!')
