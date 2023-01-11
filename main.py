import requests
import bs4

# req to get a response
res = requests.get("https://books.toscrape.com/")

# grab the source code
soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup)
