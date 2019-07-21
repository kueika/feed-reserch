import feedparser
import urllib
import requests
from bs4 import BeautifulSoup

want_rakuten = input("type your wants: ")
want_encoded = urllib.parse.quote(want_rakuten)

rakuten_url  ="https://www.kuroneko-square.net/services/rakuten/rest?keyword={}".format(want_encoded)

rakuten_dic = feedparser.parse(rakuten_url)

seikihyougen = "[ -~]+"

for entry in rakuten_dic.entries:
    title = entry.title
    link = entry.link
    print(title)
    # revRvwUserEntryCmt description
    response = requests.get(link)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, 'html.parser')
    t = bs.find_all()

