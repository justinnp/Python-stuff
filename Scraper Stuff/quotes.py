from bs4 import BeautifulSoup
import requests

def urlGen(page):
    return "http://quotes.toscrape.com/{}".format(page)

url = urlGen("")
req = requests.get(url)
res = req.status_code

quotes = []
yeet = True

while yeet:
    try:
        soup =  BeautifulSoup(req.content, "lxml")
        tomatoSoup = soup.find_all("span", {'class' : 'text'})
        for quote in tomatoSoup:
            quotes.append(quote.text.strip())
        nextPage_li = soup.find_all("li",{'class' : 'next'} )
        nextPage_a = nextPage_li[0].contents[1]
        nextPage = nextPage_a['href']
        req = requests.get(urlGen(nextPage))
    except:
        yeet = False

for quote in quotes:
    print(quote)




