import re

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
print(a)

alist = [(key,value) for (key,value) in a.items()]

sorted(alist, key=lambda tup: tup [1],reverse=True)

