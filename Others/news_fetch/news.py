from bs4 import BeautifulSoup
import requests

# fetch the news form the website :- https://www.indiatoday.in/india
#
# himanshu tripathi 
# 

page = []
url = "https://www.indiatoday.in/india"

# text file
file = open('news.txt','a')

r = requests.get(url).text
soup = BeautifulSoup(r,'lxml')

def page_change():
	for i in range(len(page)-1):
		next_page = str(page[i+1])
		url = page[i]

		# print(url)

def change_url(p):
	for i in range(len(p)):
		url = p[i]
		# print(url)

def news_fetch(url):
	
	# print(soup.prettify())
	# print(soup.title)

	# WE GOT ALL THE NEWS FORM FIRST PAGE
	for news in soup.find_all('div',class_="catagory-listing"):
		# print(news.prettify())
		 heading = news.h3.text
		 print("Heading:- " + heading)
		 file.write("Heading:- " + heading+'\n')
		 details =  news.p.text
		 print("Details:- " + details)
		 file.write("Details:- " + details+'\n')
		 link = news.find('a')
		 l = link.get('href')
		 reallink = f"{url}{l}"
		 print("Link:- "+ reallink)
		 file.write("Link:- " + reallink+'\n\n')


		 print()
		 print('\n')
		 # page_change()
		 # print(page[1])

def page_links(url):
	for new_page in soup.find_all('li',class_='pager-item'):
		new_page_link = new_page.find('a')
		new_page_link_page_link = new_page_link.get('href')
		new_page_link_real = f"{url}{new_page_link_page_link}"
		# print(new_page_link_real)
		# print()
		page.append(new_page_link_real)


page_links(url)
# print(page)


# page_change()
# print(url)
news_fetch(url)
page_change()
print(url)
change_url(page)
page_change()
print(url)
file.close()
# https://www.indiatoday.in/india/story/rss-workers-clash-with-left-activists-in-kerala-4-injured-1450060-2019-02-07