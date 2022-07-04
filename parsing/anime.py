import requests
from bs4 import BeautifulSoup


URL_anime = "https://rezka.ag/animation/"

HEADERS_3 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

}

def get_html_3(url, params=''):
    req = requests.get(url, headers=HEADERS_3, params=params)
    return req

def get_data_3(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    animation = []
    for item in items:
        animation.append({
            "title": item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            "desc": item.find('div', class_="b-content__inline_item-link").find('div').getText(),
            "link": item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            "image": item.find('div', class_="b-content__inline_item-cover").find('a').find('img').get('src'),
        })

    return animation
    #print(series)

def parser_3():
    html = get_html_3(URL_anime)
    if html.status_code == 200:
        animation = []
        for page in range(1, 2):
            # print(f"{URL}page/{page}/")
            html = get_html_3(f"{URL_anime}/page/{page}/")
            animation.extend(get_data_3(html.text))
        return animation
    else:
        raise Exception('Error in parser!!!')
