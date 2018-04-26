import requests
from bs4 import BeautifulSoup

import pickle
from pprint import pprint

# Collect first page of artists’ list
page = requests.get('http://www.pythonchallenge.com/pc/def/channel.html')

soup = BeautifulSoup(page.text, "html.parser")
soup = soup.get_text().replace("\n", "")