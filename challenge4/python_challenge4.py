import urllib2
from bs4 import BeautifulSoup

num = 8022 
counter = 0
curr = num
while(num != 0):
    counter += 1
    print (counter)
    
    quote_page = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(num)

    ipage = urllib2.urlopen(quote_page).read()

    soup = BeautifulSoup(ipage, "html.parser")

    body = soup.get_text()
    
    num = body.split()[-1]
    try:
        num = int(num)
    except:
        num = 0

print(quote_page)

