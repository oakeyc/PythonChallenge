import requests
from bs4 import BeautifulSoup

import pickle
from pprint import pprint

with open("banner.p", "rb") as file:
    color = pickle.load(file)

# Collect first page of artists’ list
page = requests.get('http://www.pythonchallenge.com/pc/def/peak.html')

soup = BeautifulSoup(page.text, "html.parser")
soup = soup.get_text().replace("\n", "")

for ob in color:
    result = ""
    for inside in ob:
        result += inside[0] * int(inside[1])
    print(result)

print("number of characters", str(counter))
print("number of soups", str(len(soup)))
print("number of lines", str(len(color)))


