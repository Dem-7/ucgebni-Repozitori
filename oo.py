import requests

from bs4 import BeautifulSoup

from nnn import response

url ="http://quotes.toscrape.com/"
response = requests.get(url)
pp = response.text
klo = BeautifulSoup(pp, "html.parser")
nn = klo.find_all("span", status_="text")
pdf = klo.find_all("small",status_="author")
for a in range(len(nn)):
    print(f"Номер цитаты - {a + 1}")