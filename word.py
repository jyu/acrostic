import urllib2
from bs4 import BeautifulSoup
import json
import random
from ginger import correct

def processWord(w):
    w = w.replace("\n", "")
    w = w.replace(".", "")
    w = w.replace(" ", "")
    return w

def filterVerbs(vList):
    res = []
    for w in vList:
        if (w.find("ing") != -1):
            # res.append(w[:-3])
            continue
        elif (w.find("ed") != -1):
            # res.append(w[:-2])
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
                        if (w != ""):
                            words.append(processWord(w))
            except:
                continue
    if (wordType == "verbs"):
        words = filterVerbs(words)
    return words


# adjective, verbs, noun, adverb
# wordLists = []
# wordLists.append(getWord("adjective", "a"))
# wordLists.append(getWord("adjective", "d"))
# wordLists.append(getWord("noun", "i"))
# wordLists.append(getWord("adverb", "n"))
# wordLists.append(getWord("verbs", "g"))
# wordLists.append(getWord("noun", "s"))

wordLists = []
wordLists.append(getWord("adjective", "f"))
wordLists.append(getWord("adjective", "e"))
wordLists.append(getWord("noun", "l"))
wordLists.append(getWord("verbs", "l"))
wordLists.append(getWord("adverb", "a"))

#wordLists.append(getWord("adjective", "m"))
#wordLists.append(getWord("noun", "e"))
#wordLists.append(getWord("verbs", "m"))
#wordLists.append(getWord("noun", "e"))
# print w3
for i in range(4):
    sentence = []
    for wl in wordLists:
        sentence.append(random.choice(wl))

    s = " ".join(sentence)
    print correct(s)

