import urllib2
from bs4 import BeautifulSoup
import json

url = "http://noun1.com/start-n/"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

c = ","
for p in soup.find_all("p"):
    if p:
        #print p
        words = str(p).split(c)
        if len(words) > 3:
            print words

