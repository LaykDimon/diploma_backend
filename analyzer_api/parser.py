import requests
from bs4 import BeautifulSoup

def get_html(url, params=None):
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36', 'accept': '*/*'}
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # habr
    items = soup.find('div', xmlns='http://www.w3.org/1999/xhtml').contents 
    # gamedeveloper
    # items = soup.find('div', class_ = 'article-content').contents
    # hackernoon
    # items = soup.find('div', class_ = 'ProseMirror')


    text = ""
    for item in items:
        text += (item.get_text() + '\n')
        print(item.get_text())
    
    return text
    # print(items)


def parse(URL):
    # links = ['https://habr.com/', 'https://www.gamedeveloper.com/']
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)
    else:
        print('Error')