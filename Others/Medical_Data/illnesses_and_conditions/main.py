# web Scrapping .. We'll get the data form  https://www.nhsinform.scot
# only education purpose only


# Himanshu Tripathi


from bs4 import BeautifulSoup
import requests

website = "https://www.nhsinform.scot"
url = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"
r = requests.get(url).text
# print(r)

soup = BeautifulSoup(r, 'lxml')
# print(soup.prettify())

file = open('links.txt', 'a')

data = soup.find("div", class_="col small-12 panel-content")

for link in data.find_all('a'):
    get_link = website + link.get('href')
    # print(website+link.get('href'))
    file.write(get_link + '\n')

file.close()
