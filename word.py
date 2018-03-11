import urllib2
from bs4 import BeautifulSoup
import json

def processWord(w):
    w = w.replace("\n", "")
    w = w.replace(".", "")
    return w

url = "http://noun1.com/start-n/"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

c = ","
words = []
for p in soup.find_all("p"):
    if p and p.string:
        try:
            s = str(p.get_text())
            parsedWords = s.split(c)
            if len(parsedWords) > 3:
                for w in parsedWords:               
                    if w != "":        
                        words.append(processWord(w))
        except:
            continue    
print words

