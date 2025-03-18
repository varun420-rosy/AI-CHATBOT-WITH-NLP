#CODTECH IT SOLUTIONS.
#TASK-3 AI CHATBOT WITH NLP.
#PROGRAM FOR SIMPLE CHATBOT USING NATURAL LANGUAGE PROCESSING.

import nltk
from nltk.stem import WordNetLemmatizer
a = WordNetLemmatizer()
import json
import numpy as np
import random
with open("task3_support.json") as b:
    c = json.load(b)
d = []
e = []
f = []
g = []
for h in c["intents"]:
    for i in h["patterns"]:
        j = nltk.word_tokenize(i)
        d.extend(j)
        f.append(j)
        g.append(h["tag"])
    if h["tag"] not in e:
        e.append(h["tag"])
d = [a.lemmatize(k.lower()) for k in d if k != "?"]
d = sorted(list(set(d)))
e = sorted(e)
def words(m, d):
    n = [0 for _ in range(len(d))]
    o = nltk.word_tokenize(m)
    o = [a.lemmatize(p.lower()) for p in o]
    for q in o:
        for r, s in enumerate(d):
            if s == q:
                n[r] = 1
    return np.array(n)
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        u = input("You: ")
        if u.lower() == "quit":
            break
        v = words(u, d)
        w = {}
        for x in c["intents"]:
            y = 0
            for z in x["patterns"]:
                aa = nltk.word_tokenize(z)
                aa = [a.lemmatize(bb.lower()) for bb in aa]
                for cc in aa:
                    if cc in u.lower():
                        y += 1
            w[x["tag"]] = y
        x = max(w, key=w.get)
        for dd in c["intents"]:
            if dd["tag"] == x:
                ee = dd["responses"]
                print(random.choice(ee))
chat()
 
