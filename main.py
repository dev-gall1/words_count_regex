import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

with open("FILE","r") as file:
  text = file.read()

patterns = re.compile("[a-zA-Z]+")

words = re.findall(patterns, text.lower())

len(words)

a = {}

for word in words:
  if word in a.keys():
    a[word] = a[word] + 1
  else:
    a[word] = 1

alist = [(key,value) for (key,value) in a.items()]

alist = sorted(alist, key=lambda tup: tup [1],reverse=True)


english_stopwords = stopwords.words("english")

listsstopwords = []

for i in english_stopwords:
  listsstopwords.append(i)


filtred = []

for i,n in alist:
  if i not in listsstopwords:
    filtred.append((i,n))


analyser = SentimentIntensityAnalyzer()

score = analyser.polarity_scores(text)

patterns = re.compile("Chapter [0-9]+")
chapters = re.split(patterns,text)

chapters = chapters[1:]

chapters = [i.replace("\n","") for i in chapters ]

print(len(chapters))


score = {}
for index,chapter in enumerate(chapters):
  score[index + 1] = analyser.polarity_scores(chapter)


print(score)