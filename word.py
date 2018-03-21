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

def getWordList(pattern, word):
    wordList = []
    for i in range(len(word) - len(pattern)):
        wordList.append(getWord("adjective", word[i]))
    for i in range(len(pattern)):
        wordList.append(getWord(pattern[i], word[i + len(word) - len(pattern)]))
    return wordList

# adjective, verbs, noun, adverb
patterns = [
["adjective", "noun", "verbs", "adverb"],
["adjective", "noun", "adverb", "verbs"],
["adjective", "noun", "verbs", "noun"],
["adjective", "noun", "adverb", "verbs", "noun"]
]

wordLists = getWordList(patterns[3], "adings")

# print w3
for i in range(4):
    sentence = []
    for wl in wordLists:
        sentence.append(random.choice(wl))

    s = " ".join(sentence)
    print correct(s)

