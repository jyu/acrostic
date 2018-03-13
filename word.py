import urllib2
from bs4 import BeautifulSoup
import json
import random

def processWord(w):
    w = w.replace("\n", "")
    w = w.replace(".", "")
    w = w.replace(" ", "")
    return w

def filterVerbs(vList):
    res = []
    for w in vList:
        if ((w.find("ing") != -1) or
            (w.find("ed") != -1)):
            continue
        elif w[-1] != "s":
            res.append(w + "s")
    return res

def getWord(wordType, letter):
    url = "http://" + wordType + "1.com/start-" + letter + "/"
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
    return words

sentence = []
sentence.append(random.choice(getWord("adjective", "m")))
sentence.append(random.choice(getWord("noun", "e")))
sentence.append(random.choice(getWord("verbs", "m")))
sentence.append(random.choice(getWord("noun", "e")))
print " ".join(sentence)
