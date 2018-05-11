from PIL import Image
from pprint import pprint

import requests
from bs4 import BeautifulSoup

page = requests.get("http://huge:file@www.pythonchallenge.com/pc/return/good.html")
soup = BeautifulSoup(page, "html.parser")

print(soup)

"""
img = Image.open('oxygen.png')

pix = img.load() # pix is a list of (R,G,B,A), which can be accessed by pix[x,y]

print(img.size)# (width, height)

center = [pix[x,img.size[1]/2] for x in range(30)] 

pprint(center)

res = [chr(pix[4,47][0])] + [chr(pix[5+7*i,47][0]) for i in range(86)]
x = ''.join(res) 

print (x)

# nums you get from the top thing
nums = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for num in nums:
    print(chr(num)) 
"""


