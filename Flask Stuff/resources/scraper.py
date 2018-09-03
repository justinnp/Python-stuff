from bs4 import BeautifulSoup
import requests

# def urlGen(page):
#     return "http://quotes.toscrape.com/{}".format(page)

def getQuotes():
    # url = urlGen("")
    url = "http://quotes.toscrape.com/"
    req = requests.get(url)

    quotes = []
    authors = []
    jsonObject = {}

    soup =  BeautifulSoup(req.content, "lxml")
    span_text = soup.find_all("span", class_="text")
    small_author = soup.find_all("small", class_="author")

    for quote in span_text:
        quotes.append(quote.text.strip())
    for author in small_author:
        authors.append((author.text.strip()))
    # nextPage_li = soup.find_all("li", class_="next" )
    # nextPage_a = nextPage_li[0].contents[1]
    # nextPage = nextPage_a['href']
    # req = requests.get(urlGen(nextPage))

    for i in range(len(authors)):
        a = {}
        a['quote'] = quotes[i]
        jsonObject[authors[i]] = a

    return jsonObject



# for quote in quotes:
#     print(quote)

# for author in authors:
#     print(author)




