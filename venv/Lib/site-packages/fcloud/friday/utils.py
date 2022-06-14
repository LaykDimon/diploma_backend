import wikipedia
import requests
from bs4 import BeautifulSoup
from math import radians, cos, sin, asin, sqrt 

from .dictionary import questions

def get_wiki_data(cmd: str) -> str:
    title = cmd
    for qn in questions:
        title = title.replace(qn, "").strip()
    title = title.replace(" ?", "").replace("?", "")
    try:
        reply = wikipedia.summary(cmd, sentences=2)
    except wikipedia.exceptions.DisambiguationError:
        reply = 'Sorry sir, Which {} are you refering to ?'.format(title.capitalize())
    except wikipedia.exceptions.PageError:
        reply = "Sorry sir, I don't know much about {}".format(title.capitalize())
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it."

    return reply


def get_weather_data() -> str:
    try:
        response = requests.get("https://www.google.com/search?q=weather+kollam%2C+kerala&oq=weather")
        html_code = response.content
        html_code = BeautifulSoup(html_code, "html.parser")
        reply = html_code.find("div", {"class", "iBp4i"}).text + ", "
        reply += html_code.find("div", {"class", "tAd8D"}).text.split("\n")[1] + ", "
        reply += html_code.find("div", {"class", "kCrYT"}).text.split(" / ")[0]
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it."
    return reply

def get_my_location() -> str:
    response = requests.get("http://ipinfo.io/loc")
    return [float(cord) for cord in response.text.replace("\n", "").split(",")]


def get_distance_btw(d1, d2) -> str: 
    # deg -> rad
    d1[1] = radians(d1[1])
    d2[1] = radians(d2[1])
    d1[0] = radians(d1[0])
    d2[0] = radians(d2[0])

    # Haversine formula  
    dlon = d2[1] - d1[1]
    dlat = d2[0] - d1[0]
    c = 2 * asin(sqrt(sin(dlat / 2)**2 + cos(d1[0]) * cos(d2[0]) * sin(dlon / 2)**2))

    # radius of earth = 6371 km or 3956 miles
    d = c * 6371 * 1000

    if d > 1000:
        distance = str(d / 1000) + " km"
    else:
        distance = str(d) + " m"
    return distance
