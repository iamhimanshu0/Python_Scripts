import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# you need to add your driver path for selenium in order to work
# in my case :- E:\Learning_Videos\chromedriver.exe

# path = 'E:\Learning_Videos\chromedriver.exe'y

# you need to add your path 


# driver = webdriver.Chrome(executable_path=path)

driver = webdriver.Chrome(executable_path="E:\Learning_Videos\chromedriver.exe")
		
file = open('links.txt','r')

links = []
for i in file:
	links.append(i)


def website_crawl(driver):
	for i in range(0,len(links)):
		data_file = driver.get(links[i])
		file_link = links[i].split('/')
		file_name = file_link[-2]
		get_data(links[i],file_name)
		
		# print()
		
		

# get the data form the website
def get_data(data_file,file_name,driver=driver):
	file_data = driver.find_element_by_class_name('guide__section')
	webData = file_data.text
	
	# print(file_name)
	with open(file_name+'.txt','w') as dataFile:
		dataFile.write(webData)			
	

	dataFile.close()



website_crawl(driver)

# print(links)

file.close()