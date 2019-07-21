import feedparser
import urllib
import requests
from bs4 import BeautifulSoup
import re

want_rakuten = input("type your wants: ")
want_encoded = urllib.parse.quote(want_rakuten)

rakuten_url = "https://www.kuroneko-square.net/services/rakuten/rest?keyword={}".format(want_encoded)

rakuten_dic = feedparser.parse(rakuten_url)

pattern = '<a.*?href="(.*?)">(.*?)'
count = 0
for entry in rakuten_dic.entries:
    if count > 5:
        break
    try:
        title = entry.title
        link = entry.link
        print(title)
        # revRvwUserEntryCmt description is wanted reveiw
        response = requests.get(link)
        response.encoding = response.apparent_encoding
        bs = BeautifulSoup(response.text, 'html.parser')
        t = bs.find("a", href=re.compile("https://review.rakuten.co.jp/item/"))
        results = re.findall(pattern, str(t), re.S)
        revlink  = str(results[0])
        print(results[0])
        print(type(results[0]))

        # res = requests.get(revlink)
        # res.encoding = res.apparent_encoding
        # bs = BeautifulSoup(res.text, "html.parser")
        # comment_tags = bs.select("revNtPtRevCmt")
        # print(comment_tags)
        #
        # count += 1
    except IndexError:
        print("skipped")


def check_review(reviewlink):
    res = requests.get(reviewlink)
    res.encoding = res.apparent_encoding
    bs = BeautifulSoup(res.text, "html.parser")
    comment_tags = bs.select("revNtPtRevCmt")
    print(comment_tags)
