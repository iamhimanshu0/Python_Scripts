

# link = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/a/abdominal-aortic-aneurysm/'

# l = link.split('/')
# print(l[-2])

link = []
# Set the links inside the link list
with open('links.txt','r') as linkFile:
	for l in linkFile:
		link.append(l)


linkFile.close()

# make the file using link name and save
# lf = 'Windows Defender Antivirus wants to restore your Chrome settings to their original defaults. This will reset your homepage, new tab page and search engine, disable your extensions, and unpin all tabs. It will also clear other temporary and cached data, such as cookies, content and site data. Learn more'

for i in range(len(link[0:1])):
	file_link = link[i].split('/')
	file_name = file_link[-2]
	# print(file_name)
	with open(file_name+'.txt','w') as file:
		file.write(file_name)
		
	file.close()


print(len(link))