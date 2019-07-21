import feedparser
import urllib
import requests
from bs4 import BeautifulSoup

want = input("enter your want thing: ")
# URLエンコードを行う
want_encoded = urllib.parse.quote(want)
url = 'https://shopping.yahoo.co.jp/rss?p={}&tab_ex=commerce&oq=&pf=&pt=&area=07&dlv=&ei=UTF-8'.format(want_encoded)

yahooshopping = feedparser.parse(url)

for entry in yahooshopping.entries:
  title = entry.title
  link  = entry.link
  print(title)
  response = requests.get(link)
  response.encoding = response.apparent_encoding
  bs = BeautifulSoup(response.text,'html.parser')
  # index = bs.find("p",attrs={"class","elItemCommentTitle"})
  # lines = index.fin
  comment_tags = bs.select(".elItemCommentText")
  for elem in comment_tags:
    print(elem)
    print(type(elem))
  print("")
